from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from events_list.models import Event, Group, Hashtag, Log, Person, Topic
from datetime import datetime, timedelta
import json
import logging
import urllib2
import sys

# Note that this API key is *my* API key (rbowen) and if we start using
# it more than a few dozen times an hour it's likely to get revoked.
# Please play nice.
# This is now Mara's key
# FIXME: make this a configuration value
MEETUP_API_KEY = "6e342d7c12183a6438e106a5b66217"

logger = logging.getLogger(__name__)

def home(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    template = loader.get_template('home.html')
    context = RequestContext(request, {
                             'state': state,
                             'username': username
    })
    return HttpResponse(template.render(context))

def index(request):
    now = datetime.now()
    upcoming_events_list = Event.objects.filter(is_applicable = True).filter(local_start__gte=now).order_by('local_start')
    template = loader.get_template('events/index.html')
    context = RequestContext(request, {
                             'upcoming_events_list': upcoming_events_list,
                             'can_import': _canImport()
    })
    return HttpResponse(template.render(context))

def eventSearch(request):
    return render(request, 'events/eventSearch.html')	

def createAccount(request):
    return render(request, 'events/createAccount.html')
	
# Lists the events for the next 14 days
def eventList(request):
    now = datetime.now()
    td = timedelta(days = 14)
    enddate = now + td
    upcoming_events = Event.objects.filter(is_applicable = True).filter(local_start__lte=enddate).filter(local_start__gte=now).order_by('local_start')
    markdown = ""
    for event in upcoming_events:
        markdown = markdown + '  * ' + event.markdown

    return HttpResponse(markdown, content_type="text/plain")
    
# Views a specific event
def viewEvent(request, event_id):
    event = get_object_or_404(Event, pk = event_id)

    template = loader.get_template('events/view.html')
    context = RequestContext(request, {
                             'event': event
    })
    return HttpResponse(template.render(context))
    
# Toggle the is_applicable field on a given record
def toggleEventNA(request, event_id):
    event = get_object_or_404(Event, pk = event_id)
    event.is_applicable = not event.is_applicable
    event.save()

    log = Log();
    desc = "Event (id=" + event_id + ") marked as "
    if (event.is_applicable):
        desc = desc + "applicable "
    else:
        desc = desc + "not applicable "
    log.description = desc;
    log.object_id = event_id
    log.action_type = Log.EVENT_UPDATE
    log.save()

    return redirect('events_list.views.index')

# Lists all the groups
def groupIndex(request):
    groups_list = Group.objects.all().filter(is_applicable = True)
    template = loader.get_template('groups/index.html')
    context = RequestContext(request, {
                             'groups_list': groups_list,
                             'can_import': _canImport()
    })
    return HttpResponse(template.render(context))

# Toggle the is_applicable field on a given record
def toggleGroupNA(request, id):
    group = get_object_or_404(Group, pk = id)
    group.is_applicable = not group.is_applicable
    group.save()

    log = Log();
    desc = "Group (id=" + id + ") marked as "
    if (group.is_applicable):
        desc = desc + "applicable "
    else:
        desc = desc + "not applicable "
    log.description = desc;
    log.object_id = id
    log.action_type = Log.GROUP_UPDATE
    log.save()

    events = Event.objects.filter(group = group)
    for event in events:
        event.is_applicable = group.is_applicable
        event.save()

    return redirect('events_list.views.groupIndex')

# Lists all the people
def personIndex(request):
    person_list = Person.objects.all()
    template = loader.get_template('people/index.html')
    context = RequestContext(request, {
                             'person_list': person_list
    })
    return HttpResponse(template.render(context))    

# Shows a specific person's information
def viewPerson(request, person_id):
    person = get_object_or_404(Person, pk = person_id)

    template = loader.get_template('people/view.html')
    context = RequestContext(request, {
                             'person': person
    })
    return HttpResponse(template.render(context))


def _canImport():
    if settings.DEBUG:
        td = timedelta(microseconds = 1)
    else:
        td = timedelta(hours = 1)
    
    can_import = True
    now = datetime.now()
    try:
        last_import = Log.objects.filter(action_type = Log.EVENT_IMPORT)[:1].get()
        if now - last_import.datetime < td:
            can_import = False
    except:
        pass
    return can_import

def importMembers(request, group_id):
    group = get_object_or_404(Group, pk = group_id)

    # Import members of a given group
    log = Log()
    log.description = "Members imported"
    log.action_type = Log.EVENT_IMPORT
    log.save()

    url = "https://api.meetup.com/2/members?offset=0&format=json&group_id=" + str(group.meetupID) + "&photo-host=public&page=500&sig_id=148657742&key=" + MEETUP_API_KEY
    response = urllib2.urlopen(url)
    result = response.read()

    data = json.loads(result)
    members = data['results']

    for member in members:
        try:
            person = Person.objects.get(meetupID = member['id'])
        except Person.DoesNotExist:
            person = Person()

        try:
            person.meetupID = member['id']
            person.name = member['name']
            person.country = member['country']
            if 'state' in member.keys():
                person.state = member['state']
            person.city = member['city']
            if 'lon' in member.keys():
                person.longitude = member['lon']
            if 'lat' in member.keys():
                person.latitude = member['lat']                
            person.url = member['link']
            if 'bio' in member.keys():
                person.bio = member['bio']
            visited = float(str(member['visited'])[0:-3])
            person.lastVisit = datetime.utcfromtimestamp(visited)
            if 'photo' in member.keys():
                if 'highres_link' in member['photo'].keys():
                    person.largePhoto = member['photo']['highres_link']
                if 'photo_link' in member['photo'].keys():
                    person.photo = member['photo']['photo_link']
                if 'thumb_link' in member['photo'].keys():
                    person.thumbnail = member['photo']['thumb_link']
            person.save()

            if 'topics' in member.keys():
                for topic in member['topics']:
                    try:
                        record = Topic.objects.get(meetupID = topic['id'])
                    except Topic.DoesNotExist:
                        record = Topic()
                    record.urlkey = topic['urlkey']
                    record.name = topic['name']
                    record.meetupID = topic['id']
                    record.save()
                    person.topics.add(record)
            

            person.groups.add(group)
            person.save()
        except:
            print('Unable to save Person object: '), sys.exc_info()[0], sys.exc_info()[1]

    return redirect('groupIndex')

def importMeetups(request):
    # Import latest meetups from meetup.com, if we didn't import them within the last hour
    log = Log()
    log.description = "Events imported"
    log.action_type = Log.EVENT_IMPORT
    log.save()

    # get all the hashtags from the DB
    hashtags = Hashtag.objects.all().exclude(name = "Meetup")

    # iterate over them all makeing a call to meetups.com for each one and adding results to the database
    for hashtag in hashtags:
      _callMeetupsCom(hashtag)

    return redirect('eventIndex')

def _callMeetupsCom(hashtag):
    print "searching meetups.com for " + hashtag.name

    # Radius is defined around Lexington, KY, but it's infinite radius, so
    # should work everywhere.
    url = "https://api.meetup.com/2/open_events?&sign=true&photo-host=public&state=ky&city=lexington&country=usa&topic=" + hashtag.name + "&radius=10000&sign=true&key=" + MEETUP_API_KEY

    print "Fetching meetups ..."

    response = urllib2.urlopen(url)
    m = response.read()

    print "Parsing results ..."
    r = json.loads(m)
    meetups = r['results']

    groups = {}

    print "Fetching group details ..."

    for meetup in meetups:
        groups[ str( meetup['group']['id'] ) ] = meetup['group']['name']
    
    keys = groups.keys()
    keyarg = ",".join( keys )
    
    group_url = "https://api.meetup.com/2/groups?&sign=true&photo-host=public&group_id=" + keyarg + "&key=" + MEETUP_API_KEY

    response = urllib2.urlopen( group_url )
    m = response.read()
    r = json.loads(m)

    grps = r['results']

    grp_deets = {}
    for g in grps:
        grp_deets[ g['id'] ] = g

    # Remove duplicate entries (where duplicates are defined by events
    # with the same name at the same UTC time (some groups spam
    # meetups.com with multuple entries)
    for meetup in meetups:
        for m in meetups:
            if meetup['id'] != m['id']:
                if meetup['name'] == m['name']:
                    if meetup['time'] == m['time']:
                        if meetup['utc_offset'] == m['utc_offset']:
                            meetups.remove(m)
                            
    for meetup in meetups:
        # Group information
        grp = grp_deets[ meetup['group']['id'] ]

        try:
            group = Group.objects.get(meetupID = grp['id'])
        except Group.DoesNotExist:
            group = Group()            
        
        try:
            group.meetupID = grp['id']
            group.name = unicode(grp['name'])
            group.city = unicode(grp['city'])
            if 'state' in grp.keys():
                group.state = grp['state']
            group.country = grp['country']
            group.save()
        except:
            print('Unable to save Group object: '), sys.exc_info()[0], sys.exc_info()[1]

        try:
            event = Event.objects.get(meetupID = meetup['id'])
        except Event.DoesNotExist:
            event = Event()

        try:
            event.name = unicode(meetup['name'])
            event.event_url = meetup['event_url']
            event.meetupID = meetup['id']
            event.group = group
            event.description = unicode(meetup['description'])
            start = float(str(meetup['time'])[0:-3])
            if 'duration' in meetup.keys():
                end = float(str(meetup['duration'])[0:-3])
            else:
                end = 0
            offset = float(str(meetup['utc_offset'])[0:-3])
            event.local_start = datetime.utcfromtimestamp(start + offset)
            event.local_end = datetime.utcfromtimestamp(start + end + offset)
            event.utc_offset = offset
            event.is_applicable = group.is_applicable                
            event.save()

            event.hashtags.add(hashtag)
            event.save()
        except:
            print('Unable to save Event object: '), sys.exc_info()[0], sys.exc_info()[1]

def viewTweets(request):
    return render(request, 'construction.html')
   
def tweetsNotApp(request):
    return render(request, 'construction.html')

def tweetsApp(request):
    return render(request, 'construction.html')

def construction(request):
    return render(request, 'construction.html')


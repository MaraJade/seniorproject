import datetime
from datetime import date
import urllib2
import json
import time
import re
import io

###########################
#
# Produces three files containing possible Apache-related meetups. One
# is formatted to paste onto a mailing list. One is suggested tweets.
# One is for pasting into apache.org/events/meetups.mdtext
#
# Note that these are POSSIBLY Apache-related. Typically, there's around
# a 50% false positive rate, what with hiking trails, native American
# dance enthusiasts, and heilcopter fans. These lists MUST be manually
# filtered before they are used anywhere publicly.
#
# See also note below about the API key.
#
# rbowen@apache.org 
# 29 May 2015
#
###########################

# Magic
import sys    # sys.setdefaultencoding is cancelled by site.py
reload(sys)    # to re-enable sys.setdefaultencoding()

def importMeetups():

    print "Rounding up the ponies ..."

    # Note that this API key is *my* API key (rbowen) and if we start using
    # it more than a few dozen times an hour it's likely to get revoked.
    # Please play nice.
    key = "3a7711454d145e404e531c2ee6f391d"

    # Radius is defined around Lexington, KY, but it's infinite radius, so
    # should work everywhere.
    url = "https://api.meetup.com/2/open_events?&sign=true&photo-host=public&state=ky&city=lexington&country=usa&text=apache&radius=10000&sign=true&key=" + key

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
    
    group_url = "https://api.meetup.com/2/groups?&sign=true&photo-host=public&group_id=" + keyarg + "&key=" + key

    response = urllib2.urlopen( group_url )
    m = response.read()
    r = json.loads(m)

    grps = r['results']

    print "Writing raw JSON data to 'meetups.json' and 'groups.json'"

    with io.open('meetups.json', 'w', encoding='utf-8') as raw:
        raw.write(json.dumps(meetups, indent=4, ensure_ascii=False))
        raw.close()

    with io.open('groups.json', 'w', encoding='utf-8') as raw:
        raw.write(json.dumps(grps, indent=4, ensure_ascii=False))
        raw.close();

def createFiles():
    print "Loading meetups database..."
    
    # A week for twitter and mailing list ...
    week = 7

    # Two weeks for the website
    twoweek = 14

    now = datetime.datetime.now()
    nowts  = time.mktime(now.timetuple())

    with open('meetups.json') as data_file:    
        meetups = json.load(data_file)

    with open('groups.json') as data_file:    
        grps = json.load(data_file)

    grp_deets = {}
    for g in grps:
        grp_deets[ g['id'] ] = g

    print "Ok, ready to print meetup details ..."

    weeklater = (nowts * 1000 ) + ( week * 86400 * 1000 )
    twoweeklater = (nowts * 1000 ) + ( twoweek * 86400 * 1000 )

    tweets = io. open('meetups.tweets', 'w', encoding='utf-8')
    mlist = io.open('meetups.mlist', 'w', encoding='utf-8')
    website = io.open('meetups.mdtext', 'w', encoding='utf-8')
    
    # Standard intro to mailing list post
    mlist.write( unicode('''The following are the meetups I'm aware of in the coming week where
Apache enthusiasts are likely to be present. If you know
of others, please let me know, and/or add them to
http://apache.org/events

If there's a meetup in your area, please consider attending. If you
attend, please consider taking a few photos, and possibly even writing
up a brief summary of what was covered.

--Rich

'''))
    
    for meetup in meetups:
        eventts = int( meetup['time'] + meetup['utc_offset'] )

        # Skip it if it's more than two weeks away
        if eventts > twoweeklater:
            continue

        eventtime = date.fromtimestamp( eventts/1000 )
        t = eventtime.strftime("%c");

        # Don't care about the time
        t = re.sub( ' \d\d:\d\d:\d\d \d\d\d\d', '', t );

        # Group information ...
        grp = grp_deets[ meetup['group']['id'] ]

        # For the website ...
        eventout = "* " + t + ' [' + meetup['name'] + '](' + meetup['event_url'] + "), " + grp['city'] + ', '
        if 'state' in grp.keys():
            eventout = eventout + grp['state'] + ', '
        eventout = eventout + grp['country'] + "\n"
        website.write( unicode(eventout) )
        
        # For everything else, a week is enough
        if eventts > weeklater:
            continue

        # For Twitter
        eventout = t + ' in ' + grp['city'] + ', '
        if 'state' in grp.keys():
            eventout = eventout + grp['state'] + ', '
        eventout = eventout + grp['country'] + ': ' + meetup['name'] + ' - ' + meetup['event_url'] + " #Apache #Meetup\n"
        tweets.write( unicode( eventout ))

        # For mailing list
        eventout = '* ' + t + ' in ' + grp['city'] + ', '
        if 'state' in grp.keys():
            eventout = eventout + grp['state'] + ', '
        eventout = eventout + grp['country'] + ': ' + meetup['name'] + ' - ' + meetup['event_url'] + "\n\n"
        mlist.write( unicode( eventout ))
        
    # Barn door
    tweets.close()
    mlist.close()
    website.close()

    print "Done! Check out meetups.mlist, meetups.tweet and meetups.mdtext\n"


from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Topic(models.Model):
    name = models.CharField(max_length=200)
    urlkey = models.CharField(max_length=50)
    meetupID = models.BigIntegerField(verbose_name = "Meetups.com ID", unique=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return unicode(self.name)

class Group(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=25)
    country = models.CharField(max_length=30)
    meetupID = models.BigIntegerField(verbose_name = "Meetups.com ID", unique=True)
    is_applicable = models.BooleanField(help_text = "Indicates if a group is applicable to our audience or not. If marked as not applicable meetups organized by this group will be automatically set to not applicable", default=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'{n}, {c}, {s}, {co}'.format(n=self.name, c=self.city, s=self.state, co=self.country)

class Hashtag(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return unicode(self.name)

class Person(models.Model):
    name = models.CharField(max_length = 50)
    bio = models.TextField()
    service = models.CharField(max_length = 50, default='')
    country = models.CharField(max_length = 2)
    state = models.CharField(max_length = 2)
    city = models.CharField(max_length = 30)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    url = models.URLField()
    largePhoto = models.URLField()
    photo = models.URLField()
    thumbnail = models.URLField()
    lastVisit = models.DateTimeField()
    groups = models.ManyToManyField(Group, related_name="members")
    topics = models.ManyToManyField(Topic, related_name="people")
    meetupID =  models.BigIntegerField(verbose_name = "Meetups.com ID", unique=True)
    is_applicable = models.BooleanField(help_text = "Indicates if a person is applicable to our audience or not", default=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return unicode(self.name)

class Event(models.Model):
    name = models.CharField(max_length=200)
    #added additional fields for event specific location - Justin Bruntmyer
    country = models.CharField(max_length = 2, default='')
    def save(self, force_insert=False, force_update=False):
        self.country = self.country.upper()
        super(Event, self).save(force_insert, force_update)
    state = models.CharField(max_length = 2, default='')
    city = models.CharField(max_length = 30, default='')
    address_1 = models.CharField(max_length = 40, default='')
    latitude = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    # end addition - Jusitn Bruntmyer
    event_url = models.URLField()
    group = models.ForeignKey(Group)
    meetupID = models.CharField(verbose_name = "Meetups.com ID", max_length=50, unique=True)
    description = models.TextField()
    local_start = models.DateTimeField()
    local_end = models.DateTimeField()
    utc_offset = models.BigIntegerField()
    hashtags = models.ManyToManyField(Hashtag, related_name="events")
    is_applicable = models.BooleanField(help_text = "Indicates if an event is applicable to our audience or not.", default=True)
    
    @property
    def markdown(self):
        markdown = self.local_start.strftime("%-d %b") + ' [' + unicode(self.name) + '](' + self.event_url + '), ' + unicode(self.group.city)
        if self.group.state:
            markdown = markdown + ', ' + unicode(self.group.state)
        markdown = markdown + ', ' + unicode(self.group.country) + '\n'
        return markdown

    @property
    def tweet(self):
        tweet = self.group.city + ", " + self.local_start.strftime("%-d %b") + ": " + self.name
        hashtags = self.hashtags.all()
        for hashtag in hashtags:
            tweet = tweet + " #" + hashtag.name
        tweet = tweet + " #Meetup"
        return tweet

    @property
    def date_sort(self):
        return self.local_start.strftime("%Y%m%d%H%M")

    @property
    def utc_start(self):
        td = timedelta(seconds = self.utc_offset)
        return self.local_start + td

    
    def __str__(self):
        return u'{n}, {d}'.format(n=self.name, d=self.local_start)

    def __unicode__(self):
        return u'{n}, {d}'.format(n=self.name, d=self.local_start)

class Log(models.Model):
    EVENT_UPDATE = 'EU'
    EVENT_IMPORT = 'EI'
    GROUP_UPDATE = 'GU'
    ACTION_TYPE_CHOICES = (
        (EVENT_UPDATE, 'Event Update'),
        (EVENT_IMPORT, 'Event Import'),
        (GROUP_UPDATE, 'Group Update'),
    )
    description = models.CharField(max_length=200)
    datetime = models.DateTimeField(default=datetime.now)
    action_type = models.CharField(max_length=2, 
                              choices = ACTION_TYPE_CHOICES)
    object_id = models.BigIntegerField(blank = True, null = True)
    
    def __str__(self):
        return u'{d}: {t} - {n}'.format(d=self.datetime, t=self.action_type, n=self.description)

    def __unicode__(self):
        return u'{d}: {t} - {n}'.format(d=self.datetime, t=self.action_type, n=self.description)
    
    class Meta:
        ordering = ('-datetime',)

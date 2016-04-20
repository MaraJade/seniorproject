from django.contrib import admin
from .models import Event, Group, Hashtag, Log, Person, Topic, Host, HostTopic

admin.site.register(Event)
admin.site.register(Group)
admin.site.register(Hashtag)
admin.site.register(Person)
admin.site.register(Topic)
admin.site.register(Host)
admin.site.register(HostTopic)

admin.site.register(Log)



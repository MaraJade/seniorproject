from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^index', views.index, name='eventIndex'),
    url(r'^(?P<event_id>[0-9]+)/$', views.viewEvent, name='viewEvent'),
    url(r'^(?P<event_id>[0-9]+)/toggleNA/$', views.toggleEventNA, name='toggleEventNA'),
    url(r'^importMeetups/$', views.importMeetups, name='importMeetups'),

    url(r'^events/14-days/list.md$', views.eventList, name='eventListMD'),

    url(r'^groups$', views.groupIndex, name='groupIndex'),
    url(r'^groups/(?P<id>[0-9]+)/toggleNA/$', views.toggleGroupNA, name='toggleGroupNA'),
    url(r'^groups/(?P<group_id>[0-9]+)/importMembers/$', views.importMembers, name='importMembers'),

    url(r'^people$', views.personIndex, name='personIndex'),
    url(r'^people/(?P<person_id>[0-9]+)/$', views.viewPerson, name='viewPerson'),
    url(r'^people/(?P<person_id>[0-9]+)/$', views.viewPerson, name='viewPerson'),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^createAccount/$', views.createAccount, name='createAccount'),
    url(r'^index/$', views.index, name='eventIndex'),
    url(r'^events/$', views.index, name='eventIndexLoggedIn'),
    url(r'^(?P<event_id>[0-9]+)/$', views.viewEvent, name='viewEvent'),
    url(r'^(?P<event_id>[0-9]+)/toggleNA/$', views.toggleEventNA, name='toggleEventNA'),
    url(r'^importMeetups/$', views.importMeetups, name='importMeetups'),
    url(r'^importAllHosts/$', views.importAllHosts, name='importAllHosts'),

    url(r'^eventSearch/$', views.eventSearch, name='eventSearch'),
    url(r'^events/14-days/list.md$', views.eventList, name='eventListMD'),

    url(r'^groups$', views.groupIndex, name='groupIndex'),
    url(r'^groups/(?P<id>[0-9]+)/toggleNA/$', views.toggleGroupNA, name='toggleGroupNA'),
    url(r'^groups/(?P<group_id>[0-9]+)/importMembers/$', views.importMembers, name='importMembers'),

    url(r'^people/$', views.personIndex, name='personIndex'),
    url(r'^eventHosts/$', views.eventHosts, name='eventHosts'),
    url(r'^eventHosts/(?P<personHost_id>[0-9]+)/importHosts/$', views.importHosts, name='importHosts'),
    url(r'^eventHosts/(?P<personHost_id>[0-9]+)/$', views.viewHost, name='viewHost'),
    url(r'^notEventHosts/$', views.notEventHosts, name='notEventHosts'),
    url(r'^people/(?P<person_id>[0-9]+)/toggleNA/$', views.togglePersonNA, name='togglePersonNA'),
    url(r'^people/(?P<person_id>[0-9]+)/$', views.viewPerson, name='viewPerson'),
    url(r'^people/(?P<person_id>[0-9]+)/$', views.viewPerson, name='viewPerson'),
    url(r'^tweetsNotApp', views.tweetsNotApp, name='tweetsNotApp'),
    url(r'^tweetsApp', views.tweetsApp, name='tweetsApp'),
    url(r'^tweets', views.viewTweets, name='viewTweets'),
    url(r'^construction', views.construction, name='construction'),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^logout', views.logout_view, name='logout'),
]


# ====================================================================
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ====================================================================

from django.conf.urls.defaults import *

# Where are we located?
import os
OUR_ROOT = os.path.realpath(os.path.dirname(__file__))

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$',              'nearby_people.nearby.views.welcome'),
	(r'^pick_place/$',  'nearby_people.nearby.views.pick_place'),
	(r'^find_people/$', 'nearby_people.nearby.views.find_people'),

	# Old style JSON support, not template based
	(r'^find_people_json/$', 'nearby_people.nearby.views.find_people_json'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

# Some static resources
urlpatterns += patterns('django.views.static',
    (r'^static/(?P<path>.*)$', 'serve', {'document_root':OUR_ROOT+"/static/"}),
    (r'^(favicon.ico)$', 'serve', {'document_root':OUR_ROOT+"/static/"}),
    (r'^(robots.txt)$', 'serve', {'document_root':OUR_ROOT+"/static/"}),
)

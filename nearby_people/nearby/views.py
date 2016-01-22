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

from django.http import HttpResponseRedirect
from settings import COMDEV_DOAP, SPEAKERS_DOAP, GMAPS_KEY, GEONAMES_USERNAME

from nearby_people.nearby.foaf import *
from nearby_people.nearby.forms import *
from nearby_people.nearby.shortcuts import *

import geoname
geoname.USERNAME = GEONAMES_USERNAME
#geoname.DEBUG=1

try:
   from json import dumps as json_dump
except ImportError:
   from json import write as json_dump

comdev_foaf = FOAF(COMDEV_DOAP)
speakers_foaf = FOAF(SPEAKERS_DOAP)

def welcome(request):
   form = PlaceForm()
   form.enableTypeField()
   form.initial["type"] = 'lm'

   return render(request, "welcome.html", {
      'form': form
   })

def pick_place(request):
   places = []
   message = None

   if request.POST:
		form = PlaceForm(request.POST)
		if form.is_valid():
			results = geoname.search(
						name=form.data["place_name"],
						featureClass=["P","T"],
						lang="EN",
						maxRows=10,
			)
			for res in results:
				places.append({
					'name': res['name'],
					'latitude': res['lat'],
					'longitude': res['lng'],
					'country': res['countryCode']
				})
			else:
				message = "We can't work out the location you mean, sorry. Please double check your spelling, or try searching for a nearby place which is larger."
   else:
       form = PlaceForm()
       form.set_type( request.GET.get("type","") )

   # We support html+json for responses, only html for requests
   types = ["html"]
   if request.POST:
      types.append("json")
   type = identify_type(request, types)
   mimetype = mimetypes.get(type, None)

   # Render the appropriate template
   return render(request, "pick_place.%s" % type, {
      'form': form, 'places': places, "message": message,
      'gmaps_key': GMAPS_KEY
   }, mimetype)

def retrieve_people_data(form):
   if not form.is_valid():
      return HttpResponseRedirect("/pick_place/?location_missing")

   # What do they want?
   foaf = comdev_foaf
   people_type = "Local Mentors"
   if form.data["type"] == "sp":
      foaf = speakers_foaf
      people_type = "Speakers"

   search_data = form.data
   search_latitude = float(search_data["latitude"])
   search_longitude = float(search_data["longitude"])
   rows = int(search_data["rows"])
   people = foaf.get_nearby(search_latitude, search_longitude, rows)

   # Work out the people.apache.org links for people
   for d,person in people:
      person["link"] = "http://people.apache.org/list_%s.html#%s" % \
             (person["surname"][0], person["uid"])

   # Work out our zoom
   min_lat = min( [float(d[1]["latitude"]) for d in people]+[search_latitude] )
   max_lat = max( [float(d[1]["latitude"]) for d in people]+[search_latitude] )
   min_long = min( [float(d[1]["longitude"]) for d in people]+[search_longitude] )
   max_long = max( [float(d[1]["longitude"]) for d in people]+[search_longitude] )
   center_lat = (min_lat+max_lat)/2
   center_long = (min_long+max_long)/2

   # Decide if we need to say sorry about the distances
   large_distance = False
   if len(people) > 0 and people[0][0] > 250*1000:
      large_distance = True

   # Render!
   data = {
      'location': search_data, 'people':people,
      'center_lat': center_lat, 'center_long': center_long,
      'bl_lat': min_lat, 'bl_long': min_long,
      'tr_lat': max_lat, 'tr_long': max_long,
      'large_distance': large_distance,
      'people_type': people_type,
   }
   return data
	
def find_people(request):
   data = retrieve_people_data(LocationForm(request.GET))
   data['gmaps_key'] = GMAPS_KEY

   # What format are we responding in?
   type = identify_type(request, ("html", "json", "rdf"))
   mimetype = mimetypes.get(type, None)

   # Have the appropriate data rendered
   return render(request, "people.%s" % type, data, mimetype)

def find_people_json(request):
   "Old style JSON API, using a simple JSON dump"
   data = retrieve_people_data(LocationForm(request.GET))
   return HttpResponse(json_dump(data), mimetype=mimetypes["json"])

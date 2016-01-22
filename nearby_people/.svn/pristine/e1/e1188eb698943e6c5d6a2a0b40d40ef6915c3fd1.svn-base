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

# Parses and caches foaf files

from xml.dom.minidom import parse
from settings import PEOPLE_FOAF_PATH, PEOPLE_FOAF_NAMESPACE, PEOPLE_FOAF_ALT_NAMESPACE
import datetime
import geo_helper
import sys,os
import urllib

NS_RDF = "http://www.w3.org/1999/02/22-rdf-syntax-ns"
NS_GEO = "http://www.w3.org/2003/01/geo/wgs84_pos#"
NS_FOAF = "http://xmlns.com/foaf/0.1/"
NS_DOAP = "http://usefulinc.com/ns/doap#"
NS_PM = "http://www.web-semantics.org/ns/pm#"
NS_DC = "http://purl.org/dc/elements/1.1/"

class FOAF(object):
    def __init__(self, doap_file):
        self.doap_file = doap_file
        self.people = {}
        self.updated_at = None

    def get_nearby(self, lat, long, rows = 10):
        self.ensure_data()

        dists = [
            (geo_helper.calculate_distance_and_bearing(lat,long,f["latitude"],f["longitude"])[0],f)
            for f in self.people.values()
        ]
        dists.sort( lambda x,y: int(x[0]-y[0]) )

        # If we have more than half the requested number of rows
        #  are under 1000km, then ditch the others
        km500 = 500 * 1000.0
        km1000 = 1000 * 1000.0
        km2000 = 2000 * 1000.0
        if len(dists) and dists[(rows/2)][0] <= km1000:
           dists = [d for d in dists if d[0] <= km1000]

        # If we have any results of under 500km, then skip anyone who's
        #  more than 2000km away
        if len(dists) and dists[0][0] <= km500:
           dists = [d for d in dists if d[0] <= km2000]

        return dists[:rows]

    def ensure_data(self):    
        if not self.people:
            self._refresh()
        if not self.updated_at:
            self._refresh()
        if datetime.datetime.utcnow() - self.updated_at > datetime.timedelta(hours=12):
            self._refresh()

    def _refresh(self):
        doap = parse(self.doap_file)
        foaf_people = doap.getElementsByTagNameNS(NS_FOAF,"Person")
        for foaf in foaf_people:
            uri = foaf.getAttribute("rdf:resource")
            if not uri:
                continue
            #print uri

            people_rel_uri = uri
            people_rel_uri = people_rel_uri.replace(PEOPLE_FOAF_NAMESPACE,"")
            people_rel_uri = people_rel_uri.replace(PEOPLE_FOAF_ALT_NAMESPACE,"")
            if uri != people_rel_uri and people_rel_uri.find("/") == -1:
                file = os.path.join(PEOPLE_FOAF_PATH, people_rel_uri)
                if os.path.exists(file):
                  self._parse_foaf(file, people_rel_uri)
                else:
                  sys.stderr.write("Missing FOAF file %s\n" % people_rel_uri)
            else:
                file = None
                try:
                   usock = urllib.urlopen(uri)
                   self._parse_foaf(usock, uri)
                   usock.close()        
                except IOError, e:
                   sys.stderr.write("Skipping %s due to broken server: %s\n" % (uri,e))
                
        self.updated_at = datetime.datetime.utcnow()
        
    def _parse_foaf(self, data, filename):
        surname = None
        name = None
        uid  = None
        lat  = None
        long = None
        email = None
        projects = []
        depiction = None
        weblogs = []
            
        try:
           foaf = parse(data)
        except Exception, e:
           sys.stderr.write("Skipping %s due to invalid/corrupt file: %s\n" % (filename,e))
           return None

        surnameN = foaf.getElementsByTagNameNS(NS_FOAF,"family_name")
        nameN = foaf.getElementsByTagNameNS(NS_FOAF,"name")
        longN = foaf.getElementsByTagNameNS(NS_GEO,"long")
        latN  = foaf.getElementsByTagNameNS(NS_GEO,"lat")
        uidN = foaf.getElementsByTagNameNS(NS_FOAF,"Person")
        emailN = foaf.getElementsByTagNameNS(NS_FOAF,"mbox")
        currentProjectsN = foaf.getElementsByTagNameNS(NS_FOAF,"currentProject")
        depictionN = foaf.getElementsByTagNameNS(NS_FOAF,"depiction")
        weblogsN = foaf.getElementsByTagNameNS(NS_FOAF,"weblog")
        
        if surnameN:
            surname = surnameN[0].firstChild.data
        if nameN:
            name = nameN[0].firstChild.data
            # Work out their surname from this if not given
            if not surnameN and name.find(" ") > 0:
               surname = " ".join( name.split(" ")[1:] )
        if longN:
            long = longN[0].firstChild.data
        if latN:
            lat = latN[0].firstChild.data
        if uidN:
            uid = uidN[0].getAttribute("rdf:ID")
        if depictionN:
            depiction = depictionN[0].getAttribute("rdf:resource")

        # If we got an explicit email, use the first
        if emailN:
            attr = emailN[0].getAttribute("rdf:resource")
            if attr:
                email = attr.replace("mailto:","")
            else:
                email = emailN[0].firstChild.data
        else:
            # Did we get their avail ID?
            if uid:
                email = "%s@apache.org" % uid
            else:
                # If it's not remote, then files are <avail id>.rdf
                if not filename.startswith("http"):
                    email = "%s@apache.org" % filename.split(".")[0]

        # People are funny about their lat and long
        if lat:
            if lat.endswith("N"):
                lat = lat[:-1]
            if lat.endswith("S"):
                lat = lat[:-1]
                if not lat.startswith("-"):
                    lat = "-%s" % lat
        if long:
            if long.endswith("E"):
                long = long[:-1]
            if long.endswith("W"):
                long = long[:-1]
                if not long.startswith("-"):
                    long = "-%s" % long
    
        if currentProjectsN:
            for projectN in currentProjectsN:
                projectName = projectN.getElementsByTagNameNS(NS_DOAP,"name")
                if not projectName:
                    projectName = projectN.getElementsByTagNameNS(NS_PM,"name")
                if projectName:
                    projects.append({"name": projectName[0].firstChild.data})
    
        if weblogsN:
            for weblogN in weblogsN:
                documentN = weblogN.getElementsByTagNameNS(NS_FOAF, "Document")
                if documentN:
                    url = documentN[0].getAttribute("rdf:about")
                    dt = documentN[0].getElementsByTagNameNS(NS_DC,"title")
                    if dt:
                       title = dt[0].firstChild.data
                    else:
                       title = url
                    weblogs.append({"title": title, "url": url})
    
        # Finish building up
        missing = []
        if not name:
            missing.append("name")
        if not surname:
            missing.append("surname")
        if not uid:
            missing.append("uid")
        if not lat:
            missing.append("lat")
        if not long:
            missing.append("long")

        if not missing:
            self.people[name] = {
                "name": name, "surname": surname, 
                "uid":uid, "email": email,
                "latitude": lat, "longitude": long, "projects": projects,
                "avatar": depiction, "weblogs": weblogs
            }
        else:
            sys.stderr.write("Skipping %s due to missing %s\n" % (filename,missing))

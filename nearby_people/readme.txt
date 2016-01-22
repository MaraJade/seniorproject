A web application to help with two proposed areas of effort - Local Mentors and Local Speakers.

On one side, there's a web application that people can use to find either a local mentor 
(eg someone to go to the pub with who won't know about your project, but will know about 
apache in general + any local/language things to be aware of with involvement in apache), 
or someone local who's willing to talk about the ASF. 

Behind the scenes, ASFers just need to pop the appropriate foaf:currentProject and foaf:based_near
tags in their foaf files in [2]. They then need to provide a patch for
subprojects/CommunityDevelopment.rdf and/or subprojects/ApacheSpeakers.rdf see [3].

If you're interested in having a play, it's a Django (python) web app. Just check it out [1] and
our subproject DOAP files [3] (these need to be checked out to the same directory, or you
need to update local_settings.py). You'll also need to check out the Apache Foaf files from [2], 
either put [3] into data/people or edit PEOPLE_FOAF_PATH in local_settings.py accordingly. 

Copy local_settings.py.example to local_settings.py and tell it where the checkouts are. 
Finally, do ./manage.py runserver and then http://localhost:8000/ will be it.

More information on the project, including information for people interested in signing up
or using the system, are available on the main ComDev site [4][5].

RESTful API
===========

If you want to write an alternative interface to the data we provide a RESTful API as follows:

Find people nearby
------------------

http://localhost:8000//find_people/?latitude=51.7522210026&longitude=-1.25596046448&type=lm&format=json
http://localhost:8000//find_people/?latitude=51.7522210026&longitude=-1.25596046448&type=lm&format=rdf

Will return either a JSON file or a RDF file, containing the people nearby the point defined 
in the latitude and longitude values.

Type is either "lm" for "local mentors" or "sp" for "speakers"

As well as specifying a format as a GET parameter, you can also send appropriate Content-Type or
Accept headers with your request, to select either JSON or RDF (where available)

Links
=====

[1] https://svn.apache.org/repos/asf/comdev/nearby_people
[2] https://svn.apache.org/repos/private/committers/info
[3] https://svn.apache.org/repos/private/committers/local-outreach
[4] http://community.apache.org/localmentors.html
[5] http://community.apache.org/speakers/index.html

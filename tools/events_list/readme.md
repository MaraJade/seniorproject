This directory contains tools that are useful for creating and
managing a list of events related to the ASF.

# Features #

  * Run as a script (python get_meetups) or as an interactive menu (python menu)
  * Import events from meetups.com that might be Apache related
  * Generate a mail template for events in the next 7 days
  * Generate a Markdown file for hosting on a website or similar
  * Generate a file containing suggested tweets

Run as either a Python application or as a Docker containerized
application.

# Python Script #

To run the application as a Python script simply execute get_meetups.
This will create a number of files in the project directory:

  * meetups.mlist - a template email for events in the next week
  * meetups.mdtext - a markdown file of events in the next 2 weeks
  * meetups.tweets - suggested tweets for events in the next 2 weeks
  * meetups.json - a json file of all meetups
  * groups.json - a json file containing all groups organizing meetings

Alternatively you can run the "menu" script which will present a
command line menu allowing you to work with the events list.

Note that these are POSSIBLY Apache-related. Typically, there's around
a 50% false positive rate, what with hiking trails, native American
dance enthusiasts, and heilcopter fans. These lists MUST be manually
filtered before they are used anywhere publicly.

If you use this script be respectful of the included API key.

# Docker Container #

A Docker container is provided to make it as easy as possible to work
with these scripts. To use it you must first install Docker.

To build the container:

    $ docker build -t events .

To run the container:

    $ docker run -v /path/to/host/directory:/project events

By default this runs a curses menu from which you can manage the events
list.

FIXME: Should use a data volume for the data

# Development using the Docker Container #

Edit the files on your host machine and then:

    $ docker run -it -v /path/to/host/directory:/project events

The results will be available on your host machine.


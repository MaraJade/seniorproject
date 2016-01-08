This is a Django based web application to assist with community
development.

# Features #

Currently we have a Command Line Interface and a Web Interface. At the
time of writing the CLI provides three output formats whereas the web
interface focusses on better data management.

## Command Line Features ##

  * Run as a script (python get_meetups) or as an interactive menu (python menu)
  * Import events from meetups.com that might be Apache related
  * Generate a mail template for events in the next 7 days
  * Generate a Markdown file for hosting on a website or similar
  * Generate a file containing suggested tweets

Run as either a Python application or as a Docker containerized
application.

## Web Application Features##

  * Import new meetups from meetups.com
  * Export a markdown formated list of events in the next two weeks
  * Schedule tweets via Hootsuite
  * Mark events as not applicable (will no longer appear in event lists)
  * Mark groups as not applicable (their events will never appear in event lists)
  * Import members of groups
  
# Python CLI Script #

To run the application as a Python script simply execyte get_meetups
or memu in the root of the project.
This will create a number of files in the project directory:

  * meetups.mlist - a template email for events in the next week
  * meetups.mdtext - a markdown file of events i nthe next 2 weeks
  * meetups.tweets - suggested tweets for events in the next 2 weeks
  * meetups.json - a json file of all meetups
  * groups.json - a json file containing all groups organizin meetings

Alternatively you can run the "menu" script which will present a
command line menu allowing you to work with the events list.

Note that these are POSSIBLY Apache-related. Typically, there's around
a 50% false positive rate, what with hiking trails, native American
dance enthusiasts, and heilcopter fans. These lists MUST be manually
filtered before they are used anywhere publicly.

If you use this script be respectful of the included API key.

# Development #

ALthough not required it is recommended that you use Docker to manage
your development and deployment environment as this will automatically
configure your environment for you, though it does require you to have
installed Docker.

## Without Docker ##

To work without Docker (untested please improve these docs if you go this route):

  * Install Python 2.7.x - e.g. sudo apt-get python
  * Install PostgreSQL - e.g. sudo apt-get postgresql-server-dev-9.3

  * pip install -r requirements
  * python manage.py makemigrations
  * python manage.py migrate
  * python manage.py runserver

You should now have a copy running localy on port 8000.

For more information on how the application is built you need to
understand Django. A great starting point is the [Django
tutorial](https://docs.djangoproject.com/en/1.8/intro/tutorial01/)

## With Docker

### Docker Prerequisites

You need to install Docker for local development on Linux or Mac. You
will probably want to also install docker-machine if you are going to
deploy the application.

#### For Windows

If you are using Windows as your client machine then it is a good idea
to install Git for Windows from http://msysgit.github.io/. This will
provide both Git and a Bash shell. We will use the Bash shell as a
convenience since the scripts we have built are Bash scripts.

The application is composed of a number of Docker containers.
Therefore you will need to install Docker. Docker Machine is also
useful for creating your Docker Host on which you will run your version
of the application.

On Windows open a Bash shell (search for "Unix Bash" after installing Git
for Windows):

$ curl -L https://get.docker.com/builds/Windows/x86_64/docker-latest.exe > /bin/docker
$ curl -L https://github.com/docker/machine/releases/download/v0.2.0/docker-machine_windows-amd64.exe > /bin/docker-machine

#### For Linux or Mac

See the Docker website for instructions on installing Docker and Docker 
Machine on other platforms see: http://docs.docker.com/machine/

### Docker Hosts ###

As a minimum you will need a Docker host for development. You'll most
likely want this to be on your local machine. If you are on Linux you
don't need to do anything, skip to the next section. If you are on
Windows or Mac you will need to create a Docker host on your machine.

#### Create a Docker Host on Windows

We'll use docker-machine. Run the following command (as an
administrator):

	$ docker-machine create -d hyper-v comdev

Note the "-d hyper-v" is for Windows machines, you may want to use a
different provider if you are developing on a different platform.

You'll also need to ensure that your docker client is using this
machine. Run the following command:

	$ eval "$(docker-machine env comdev)"

### Share your project code with the Docker Host

For easy development you need to ensure your project directory is
available on the Docker Host. Again, on Linux this is simple, skip
ahead to the next section. If you are on Mac or Windows there is a
little setup needed.

#### Sharing on Windows

We've provided a helper script to do this. First, create a
confiduration file:

	$ cp scripts/config.tmpl scripts/config.sh

Edit the 'config.sh' file, paying close attention to the section on
Windows share configuration.

Now run:

    $ scripts/configHyper-v.sh

The script will ask you for your Windows password and then configure
the Docker Host to share the directory you specify in .config.sh'

Once done you will not need to run this script again unless you
recreate the host.

### Build and Start Your Development Containers

As a Docker based application you will work directly with Docker
containers during development. Your local client development directory
will be mapped into /project on the container, thus local edits will
be available in your development container immediately.

The first time you run the container you will need to configure the
database. Subsequent runs will just require standard Django commands
to be run.

#### Starting the Development Containers

We've provided some scripts that will help manage this process. If you
want to see what's happening read the scripts.

To start the application in development mode run the following
command:

./scripts/deploy.sh

You will be asked where you want to deploy the application. If you are
on Linux you can respond "local". If you are on Mac or Windows you
will want to respond "dev". The difference here is that "dev" assumes
we are deploying to a docker host running in a virtual machine which
is necessary on Mac and Windows, but optional on Linux.

This script will then build and start your containers, sharing your
source directory with the container. This means you can make changes
on your development machine and see them reflected immediately on the
running applicaion container.

As with all Docker containers the first time you build and run them
the images and corresponding layers need to be downloaded. This can
take a few minutes. After the first run everything is very quick.

#### Running Django Commands

From this point development is just like any other Django application,
but to run Django commands in the app container you will need to open
a terminal on that machine. To do this run:

	$ docker exec -it comdev_app bash

### Using the Admin Interface

To access the admin interface of the application you need an admin
user account. Assuming you are starting from a clean development
container (i.e. with no data in the database) you will need to create
an admin user. To do this run the following command in your Django
terminal.

	$ python manage.py createsuperuser

Now you can log into the admin app at http://docker.host/admin

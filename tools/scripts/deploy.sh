echo "##################################################################################################"
echo "# Push a clean build of the containers to 'dev', 'stage' or 'local'"
echo "# 'dev' deploys with a mounted volume so that the source can be edited on the fly"
echo "# 'stage' deploys with a copy of the current source to the staging server"
echo "# 'local' deploys with a copy of the current source to the local host"
echo "# BEWARE: this will kill all data on the chosen machine, use with extreme caution"
echo "##################################################################################################"

source ./scripts/config.sh

read -p "What kind of deployment do you want (enter 'dev', 'stage', 'local') " type
case $type in
    "dev")
	eval "$(docker-machine env $DEV_MACHINE_NAME)"
	;;
    "stage")
	eval "$(docker-machine env $STAGE_MACHINE_NAME)"
	;;
    "local")
	;;
    *)
	echo "Unkown option, aborting"
        exit 255
	;;
esac


echo "DOCKER_HOST is set to $DOCKER_HOST"
echo "DOCKER_MACHINE_NAME is set to $DOCKER_MACHINE_NAME"
echo "Do you really want to start clean containers on this machine?"
read -p "Remember, it will destroy all data.\n Enter 'Yes' to confirm: " CONFIRM

if [ $CONFIRM != "Yes" ]; then
  echo "Phew!!! That was close, aborting"
  exit 1
fi

echo "##################################################################################################"
echo "# Remove old dev containers that may still be running"
echo "##################################################################################################"
docker rm -f meetups_db
docker rm -f meetups_app

echo "##################################################################################################"
echo "# Start the database container"
echo "##################################################################################################"
case $type in
    "dev")
	docker run -d -v //home/docker/project:/project -p 5432:5432 --name meetups_db postgres
	;;
    "stage")
	docker run -d -p 5432:5432 --name meetups_db postgres
	;;
    "local")
	docker run -d -p 5432:5432 --name meetups_db postgres
	;;
esac
sleep 3 # a small delay to ensure the DB hads time to start before we try to conenct to it

echo "##################################################################################################"
echo "# Build the application container"
echo "##################################################################################################"
docker build -t meetups .

echo "##################################################################################################"
echo "# Configure the database"
echo "##################################################################################################"
case $type in
    "dev")
	docker run --rm -v //home/docker/comdev/meetups:/project --link meetups_db:db meetups python manage.py makemigrations events_list
	docker run --rm -v //home/docker/comdev/meetups:/project --link meetups_db:db meetups python manage.py migrate
	;;
    "stage")
	docker run --rm --link meetups_db:db meetups python manage.py makemigrations events_list
	docker run --rm --link meetups_db:db meetups python manage.py migrate
	;;
    "local")
	docker run --rm -v `pwd`:/projects --link meetups_db:db meetups python manage.py makemigrations events_list
	docker run --rm -v `pwd`:/projects  --link meetups_db:db meetups python manage.py migrate
	;;
esac

echo "##################################################################################################"
echo "# Setup a superuser (hit return to continue once created)"
echo "##################################################################################################"
docker run --rm -it --link meetups_db:db meetups python manage.py createsuperuser

echo "##################################################################################################"
echo "# Run the application"
echo "##################################################################################################"
case $type in
    "dev")
	docker run --rm -v //home/docker/comdev/meetups:/project --link meetups_db:db -p 80:8000 --name meetups_app meetups python manage.py runserver 0.0.0.0:8000
	;;
    "stage")
	docker run -d --link meetups_db:db -p $STAGE_PORT:8000 --name meetups_app meetups python manage.py runserver 0.0.0.0:8000
	;;
    "local")
	docker run -d -v `pwd`:/project --link meetups_db:db -p 80:8000 --name meetups_app meetups python manage.py runserver 0.0.0.0:8000
	;;
esac

echo "##################################################################################################"
echo "# Assuming no errors above your application is now running."
echo "# You should first create one or more hashtags and then import some meetups"
echo "##################################################################################################"

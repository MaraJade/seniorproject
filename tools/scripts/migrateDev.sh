echo "##################################################################################################"
echo "# Migrate the database"
echo "##################################################################################################"

source scripts/config.sh

docker-machine env $DEV_MACHINE_NAME
eval "$(docker-machine env $DEV_MACHINE_NAME)"

docker exec meetups_app python manage.py makemigrations events_list
docker exec meetups_app python manage.py migrate

echo "##################################################################################################"
echo "# Done"
echo "##################################################################################################"

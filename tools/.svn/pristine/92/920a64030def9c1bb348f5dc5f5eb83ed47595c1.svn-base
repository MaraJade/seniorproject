###########################################################################
# Setup the machine you need to run the demo's here
###########################################################################

source ./scripts/config.sh

echo "##########################################################################################"
echo "Creating "$DEV_MACHINE_TYPE" machine for development with name $DEV_MACHINE_NAME"
echo "##########################################################################################"

docker-machine create -d $DEV_MACHINE_TYPE $DEV_MACHINE_NAME
docker-machine env $DEV_MACHINE_NAME

echo "##########################################################################################"
echo "Creating "$STAGE_MACHINE_TYPE" machine for staging with name $STAGE_MACHINE_NAME"
echo "##########################################################################################"

case "$STAGE_MACHINE_TYPE" in
  azure) docker-machine create -d azure --azure-location="$AZURE_LOCATION" --azure-subscription-id="$AZURE_SUBSCRIPTION_ID" --azure-subscription-cert="$AZURE_CERT_NAME" $STAGE_MACHINE_NAME
	 ;;
  *) echo "ERROR: Cannot create machine of type $STAGE_MACHINE_TYPE"
     ;;
esac

echo "Unless an error is reported above your VM is now ready to use"
echo "Remember, you will need to open appropriate endpoints on your VM if you want to access Docker containers from elsewhere"

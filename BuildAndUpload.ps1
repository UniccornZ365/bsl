az login --tenant ea61630a-a985-4020-8602-e6fd21fc1462
az acr login -n blueboxes

docker build --tag zoebsl:latest .
docker tag zoebsl blueboxes.azurecr.io/zoebsl:latest
docker push blueboxes.azurecr.io/zoebsl:latest
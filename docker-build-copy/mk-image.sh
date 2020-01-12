#!/bin/sh

builder="builder:latest"
prod="prodimage:latest"

echo "Build the app docker image:"
docker build -f build.Dockerfile --no-cache -t $builder .

echo "Create a container: appdata"
docker container create --name appdata $builder
docker container cp appdata:/app/bin dist
docker container rm -f appdata

echo "Build the production image"
docker build -f prod.Dockerfile --no-cache -t $prod .
rm -rf ./dist

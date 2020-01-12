#!/bin/sh
# Venky, 11/09/2019

echo "Build the production image"
docker build  --no-cache -t "production:latest" .

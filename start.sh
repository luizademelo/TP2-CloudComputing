#!/bin/bash

# docker network create tp2-network

# Build API image
docker build -t flask-api -f Dockerfile.api .
# docker run --rm -d --name flask-api --network tp2-network flask-api
docker run -d --name flask-api -p 52049:52049 flask-api

# Build Client image
docker build -t client -f Dockerfile.client .
# docker run --rm --name client --network tp2-network client
docker run --rm --name client client

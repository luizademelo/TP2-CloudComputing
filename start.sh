#!/bin/bash

# Build Model image
docker build -t model -f Dockerfile.model .
docker run --rm --name model model

# Build API image
docker build -t flask-api -f Dockerfile.api .
docker run --rm -d --name flask-api -p 52049:52049 flask-api

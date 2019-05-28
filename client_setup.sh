#!/bin/bash

cd T1-TARSD/docker_client
sudo docker build -t app_client .
sudo docker run app_client

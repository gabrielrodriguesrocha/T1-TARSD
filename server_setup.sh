#!/bin/bash

cd T1-TARSD/docker_server
sudo docker build -t app_server .
sudo docker run app_server

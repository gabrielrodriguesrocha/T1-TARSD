#!/bin/bash

cd T1-TARSD/docker_server
sudo docker swarm init --advertise-addr 192.168.50.2:2377 | sed 5!d > /vagrant/token/join.sh
sudo docker build -t app_server .
sudo docker network create -d overlay --subnet 10.0.10.0/24 ClusterNet
sudo docker service create --name app_server_service --network ClusterNet --replicas 3 -p 5001:80 app_server

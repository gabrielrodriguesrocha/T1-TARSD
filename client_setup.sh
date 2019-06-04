#!/bin/bash

sudo apt install python3 python3-pip
pip3 install bottle docker
cd T1-TARSD/docker_client
chmod +x /vagrant/join.sh
bash /vagrant/token/join.sh
sudo docker build -t app_client .
sudo docker service create --name app_client_service --network ClusterNet --replicas 3 -p 5001:80 app_client
sudo python3 info_server.py
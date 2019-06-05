#!/bin/bash

sudo apt install -y python3 python3-pip
pip3 install bottle docker
cd T1-TARSD/docker_client
chmod +x /vagrant/token/join.sh
bash /vagrant/token/join.sh
sudo docker build -t app_client .
sudo python3 info_server.py &
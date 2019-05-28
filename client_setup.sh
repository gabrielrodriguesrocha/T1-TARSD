#!/bin/bash

cd T1-TARSD/docker_client
chmod +x /opt/join.sh
bash /opt/join.sh
sudo docker build -t app_client .
sudo docker service create --name app_client_service --network ClusterNet --replicas 3 -p 5001:80 app_client

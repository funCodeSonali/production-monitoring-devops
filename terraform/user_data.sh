#!/bin/bash
apt update -y
apt install -y docker.io docker-compose-plugin git

systemctl start docker
systemctl enable docker
usermod -aG docker ubuntu

cd /home/ubuntu
git clone https://github.com/funCodeSonali/production-monitoring-devops.git
cd production-monitoring-devops

docker compose up -d

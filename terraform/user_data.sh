#!/bin/bash
# Update packages
apt update -y
apt install -y git curl

# Install official Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Enable Docker service
systemctl start docker
systemctl enable docker

# Add ubuntu user to docker group
usermod -aG docker ubuntu

# Go to home folder and clone repo
cd /home/ubuntu
if [ ! -d "production-monitoring-devops" ]; then
    git clone https://github.com/funCodeSonali/production-monitoring-devops.git
fi
cd production-monitoring-devops

# Launch Docker Compose stack
sudo docker compose up -d

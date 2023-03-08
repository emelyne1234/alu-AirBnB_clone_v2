#!/usr/bin/env bash
"""bash scripts"""
apt-get -y update
apt-get -y upgrade
apt-get -y install nginx
mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Testing html" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
service nginx start

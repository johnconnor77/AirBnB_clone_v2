#!/usr/bin/env bash
#Write a Bash script that sets up your web servers
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo -e '<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello to all</title>
</head>
<body>
<h1>Config web server</h1>
</body>
</html>' | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R 777 ubuntu:ubuntu /data
sudo sed -i "/# Only/ i location /hbnb_static {\nalias /data/web_static/current;\n}" /etc/nginx/sites-enabled/default
sudo service nginx 

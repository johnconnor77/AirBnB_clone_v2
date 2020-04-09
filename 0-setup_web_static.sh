#!/usr/bin/env bash
#Write a Bash script that sets up your web servers
#for the deployment of web_static.
# 1 step: Install Nginx if it not already installed
sudo apt-get -y update
sudo apt-get -y install nginx
# 2 set: Create the folder if it doesn’t already exist
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
# 3 step: Create a fake HTML file 
# /data/web_static/releases/test/index.html 
# (with simple content, to test your Nginx configuration)
sudo echo -e  "<!DOCTYPE html>\
<html lang=\"en"\>
<head>
    <meta charset=\"UTF-8"\>
    <meta name=\"viewport"\ content="width=device-width, initial-scale=1.0">
    <title>Hello to all</title>
</head>
<body>
<h1>Config web server</h1>
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html
# 4 step: Create a symbolic link /data/web_static/current
# linked to the /data/web_static/releases/test/ folder.
# If the symbolic link already exists, it should be deleted
# and recreated every time the script is ran.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# 5 step: Give ownership of the /data/ folder to the
# ubuntu user AND group (you can assume this user and
# group exist). This should be recursive; everything
# inside should be created/owned by this user/group.
sudo chown -R 777 ubuntu:ubuntu /data
# 6 step: Update the Nginx configuration to serve the content 
# of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static).
# Don’t forget to restart Nginx after updating the configuration:
# Use alias inside your Nginx configuration
sudo sed -i "/# Only/ i location /hbnb_static {\nalias /data/web_static/current;\n}" /etc/nginx/sites-enabled/default
sudo service nginx 

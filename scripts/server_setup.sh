#!/usr/bin/bash
sudo yum -y update
sudo yum install python-devel make automake nginx gcc gcc-c++ python-setuptools git
sudo easy_install pip
sudo pip install uwsgi virtualenv
virtualenv /var/www/assistsearch/env

git clone git@github.com:CrowdRescueHQ/Assisted-Search.git /var/www/assistsearch/app
. /var/www/assistsearch/env/bin/activate

sudo cp /var/www/assistsearch/app/nginx.conf /etc/nginx/sites-enabled/assistsearch.conf
sudo cp /var/www/assistsearch/app/uwsgi.conf /etc/uwsgi/apps/assistsearch.ini
service nginx start

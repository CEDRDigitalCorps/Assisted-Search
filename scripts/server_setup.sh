#!/usr/bin/bash
sudo apt-get update
sudo apt-get install python-dev python-pip nginx
sudo -H pip install --upgrade pip
sudo -H pip install virtualenv uwsgi
sudo mkdir -p /etc/uwsgi/sites
sudo mkdir -p /var/log/uwsgi/apps
sudo virtualenv /var/www/assistsearch/env
. /var/www/assistsearch/env/bin/activate
git clone https://github.com/CrowdRescueHQ/Assisted-Search.git /var/www/assistsearch/app
cd /var/www/assistsearch/
pip install -r requirements/base.txt
cp nginx.conf /etc/nginx/sites-enabled/assistsearch.conf
cp uwsgi.ini /etc/uwsgi/sites/assistsearch.ini
cp uwsgi.service /etc/systemd/system/uwsgi.service
sudo systemctl restart nginx
sudo systemctl start uwsgi

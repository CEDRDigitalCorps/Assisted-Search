#!/usr/bin/bash
source /var/www/assistsearch/env/bin/activate
cd /var/www/assistsearch/app
git pull origin master
pip install -r requirements/base.txt
python manage.py migrate
python manage.py collectstatic --noinput
chown -R www-data:www-data /var/www/assistsearch/app
systemctl restart uwsgi

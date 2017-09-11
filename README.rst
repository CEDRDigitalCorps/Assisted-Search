CrowdRescue
===========

Setup
-----

.. code-block:: bash

   $ pip install -r requirements/base.txt

   $ python manage.py migrate

   $ python manage.py runserver


Server
------

Setup
~~~~~

.. code-block:: bash

   $ scripts/server_setup.sh

Update
~~~~~~

.. code-block:: bash

   $ sudo -i
   $ source /var/www/assistsearch/env/bin/activate
   $ cd /var/www/assistsearch/app
   $ git pull origin master
   $ pip install -r requirements/base.txt
   $ python manage.py migrate
   $ python manage.py collectstatic --noinput
   $ chown -R www-data:www-data /var/www/assistsearch/app
   $ systemctl restart uwsgi

   or

   $ sudo -i
   $ /var/www/assistsearch/app/scripts/update.sh


Set Domain Name
~~~~~~~~~~~~~~~

Once we have a domain name we can set it up with the following changes;

    1. Update the ``settings.py``, adding the domain name to the list of ``ALLOWED_HOSTS``

    2. Update the ``nginx.conf``, replace the IP address (``45.55.140.205``) with domain name

    3. Push changes to master

    4. Deploy to server following ``Update`` steps above

    5. Lastly run the following to put the nginx conf file in place, and restart nginx;

On the server, do the following

.. code-block:: bash

   $ sudo -i
   $ cp /var/www/assistsearch/app/nginx.conf
   $ nginx -t   <-- should see syntax ok notice
   $ systemctl reload nginx

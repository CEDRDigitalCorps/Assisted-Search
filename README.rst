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

Update:

.. code-block:: bash

   $ sudo -i
   $ source /var/www/assistsearch/env/bin/activate
   $ cd /var/www/assistsearch/app
   $ git clone origin master
   $ python manage.py migrate
   $ python manage.py collectstatic --noinput
   $ chown -R www-data:www-data /var/www/assistsearch/app
   $ systemctl restart uwsgi

CrowdRescue
===========

Setup
-----

.. code-block:: bash

   $ pip install -r requirements/base.txt

   $ python manage.py migrate

   $ python manage.py runserver

Configuration
-------------

Twitter and Slack credentials are needed, create a ``settings.ini`` file with the following contents;

.. code-block:: bash

   [settings]
   TWITTER_KEY=<your-twitter-key>
   TWITTER_SECRET=<your-twitter-secret>
   TWITTER_ACCESS_TOKEN=<your-twitter-access-token>
   TWITTER_ACCESS_TOKEN_SECRET=<your-twitter-access-token-secret>
   SLACK_TOKEN=<your-slack-token>
   DATABASE_NAME=<db-table>
   DATABASE_HOST=
   DATABASE_TABLE=<db-table>  <-- used by spicey
   DATABASE_USER=<db-user>
   DATABASE_PASSWORD=

Replacing the ``<*>`` strings with relevant keys, secrets, and tokens


Server
------

Setup
~~~~~

.. code-block:: bash

   $ scripts/server_setup.sh

NTLK Download
~~~~~~~~~~~~~

.. code-block:: bash

   $ python -c "import nltk; nltk.download('punkt')"
   $ mv /root/ntlk_data /var/www/ntlk_data <-- take note where the above command saved the files, and modify the ``/root/ntlk_data`` accordingly


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

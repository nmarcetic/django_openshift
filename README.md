Django_OpenShift
===========

Django ready project structure for OpenShift.

- Django with REST service (session and token auth).
- AngularJS (service/controllers/routing/animate).
- Twitter bootstrap.
- django-compressor.

**My Django app on OpenShift**

Read OpenShift doc for rhc tool and how to push PJ with git.

**Go to settings config and def db parameters (settings/prod.py)**

**Make sure you are importing right settings file, check settings/__init__.py**

**Sync db**

$ source python/virtenv/bin/activate

cd app-root/runtime/repo/wsgi

python manage.py syncdb --noinput

**All static files are located at wsgi/static , djago-compressor will also copy all js and css files to wsgi/static/resources.**

**You can manually copy all your other static files like fonts, etc... to wsgi/static/ , so wsgi can serve to clients.**

TODO: fix this :) , implement grunt task runner!

You can create .httaccess in wsgi directory.

**Deploy to OpenShift**

cd thenameofyourapp

git add .

git commit -m "my app init commit."

gut push

**If you need a shell**

1. ssh to your OpenShift app

2. Activate virtualenv 

$ source python/virtenv/bin/activate

3. Navigate to your runtime app

cd app-root/runtime/repo/wsgi

4. python manage.py shell (or syncdb , migrate etc...)


**READ OpenShift doc and blog for more info**
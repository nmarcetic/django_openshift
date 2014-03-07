from django.conf.urls import patterns, include, url
from django.conf import settings
from .views import (ping)
urlpatterns = patterns('',
 	# Rest auth urls
 	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
 	# api urls
 	url(r'^ping/$', ping, name='ping'),
 )

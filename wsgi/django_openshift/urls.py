from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # SPA url:
    url(r'^$', 'django_openshift.apps.core.views.index', name='index'),
 	# Rest urls
 	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
 	url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
 	# test api
 	url(r'^api/', include('django_openshift.apps.api.urls', namespace='api')),
 	# Enable django admin
    url(r'^admin/', include(admin.site.urls)),
)

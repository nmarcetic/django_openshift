# -*- coding: utf-8 -*-
"""
Module handling our API .
"""
# Some base import
from django.http import HttpResponse
import datetime
from django.utils.timezone import utc
from django.contrib.auth import (login as auth_login, logout as auth_logout,
	authenticate, get_user_model)
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

# Import rest modules 
from rest_framework import status
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, AllowAny


from django_openshift.apps.accounts.models import *

# def some api message
HELLO = "Hello remote client!"
NOT_AUTHORIZED = "You are NOT authorized!"
AUTHORIZED = "You are AUTHORIZED!"

### API demo ###

# Ping service, allow any remote client to ping service
@api_view(['GET'])
@permission_classes((AllowAny, ))
def ping(request):
	msg = HELLO
	ip = request.META['REMOTE_ADDR']
	def chk_user():
		if request.user.is_authenticated():
			return AUTHORIZED
		else:
			return NOT_AUTHORIZED
	content = {
		'msg':msg,
		'ip': 'Your ip is: ' + ip,
		'auth':chk_user()
		}
	return Response(content)


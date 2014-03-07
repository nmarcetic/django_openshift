# -*- coding: utf-8 -*-
"""
Module handling our core views .
"""
from django.template.response import TemplateResponse
import datetime
from django.utils.timezone import utc

# Import rest modules 
from rest_framework import status
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions

# Dummy home page view
def index(request):
	# Return index page
	response = TemplateResponse(request, 'core/spa.html', {})
	return response

	
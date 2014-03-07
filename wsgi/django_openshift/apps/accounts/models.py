# -*- coding: utf-8 -*-
"""
Users models .
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, User

from rest_framework import serializers

# User model serializer

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('username','email','password')

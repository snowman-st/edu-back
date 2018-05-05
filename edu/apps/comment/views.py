from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .models import info_package_from
from .serializers import InfopackfromSerializer

class InfopackfromViewset(mixins.ListModelMixin,viewsets.GenericViewSet):
	'''
	获取资源包来源信息
	'''

	queryset = info_package_from.objects.all()
	serializer_class = InfopackfromSerializer
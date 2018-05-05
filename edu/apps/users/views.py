from django.shortcuts import render

# Create your views here.
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from random import choice
from rest_framework import permissions
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler

from .serializers import UsersSerializer

User = get_user_model()

class UserViewset(CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
	serializer_class = UsersSerializer
	queryset = User.objects.all()
	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication )

	def create(self,request,*args,**kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = self.perform_create(serializer)

		re_dict = serializer.data
		payload = jwt_payload_handler(user)
		re_dict["token"] = jwt_encode_handler(payload)
		re_dict["username"] = user.name if user.name else user.username

		headers = self.get_success_headers(serializer.data)
		return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)


	def get_object(self):
		return self.request.user

	def perform_create(self,serializer):
		return serializer.save()
   	
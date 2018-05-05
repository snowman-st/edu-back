#encoding:utf-8
__author__ = 'snowman'

from rest_framework import serializers
from django.db.models import Q

from comment.models import info_package_from

class InfopackfromSerializer(serializers.ModelSerializer):
	class Meta:
		model = info_package_from
		fields = "__all__"

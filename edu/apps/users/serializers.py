from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

User = get_user_model()

class UsersSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,validators=[UniqueValidator(queryset=User.objects.all(), message="该用户名已被占用！")])
    password = serializers.CharField(style={'input_type': 'password'},help_text="密码", label="密码", write_only=True,)
    
    def create(self,validated_data):
        user = super(UsersSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username','mobile','password')

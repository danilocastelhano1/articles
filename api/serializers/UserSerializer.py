from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        new_pass = make_password(validated_data['password'])
        validated_data['password'] = new_pass

        return super(UserSerializer, self).create(validated_data)

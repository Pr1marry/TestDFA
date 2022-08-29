from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Galary


# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView


class GalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Galary
        fields = '__all__'


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'pk', 'status')

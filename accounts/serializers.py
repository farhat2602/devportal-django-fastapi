from rest_framework import serializers

from accounts.models import CustomUser, Company, Technologies, Badges, Profile


class CustomUserSerializer(serializers.ModelSerializer):
    pass
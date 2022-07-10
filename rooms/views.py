from django.shortcuts import render
from rest_framework import generics

from rooms.models import Teams
from rooms.serializers import TeamsSerializer


class TeamCreateView(generics.CreateAPIView):
    serializer_class = TeamsSerializer


class TeamsListView(generics.ListAPIView):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer

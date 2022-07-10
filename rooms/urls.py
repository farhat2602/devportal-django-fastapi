from django.urls import path

from rooms.views import TeamCreateView, TeamsListView

urlpatterns = [
    path('create/', TeamCreateView.as_view()),
    path('list/', TeamsListView.as_view()),
]

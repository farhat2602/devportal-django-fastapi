from django.urls import path

from accounts.views import CustomUserRegisterView, CustomUserLoginView, CustomUserLogoutView, UserProfileView, \
    CustomUserList

urlpatterns = [
    path('register/', CustomUserRegisterView.as_view()),
    path('login/', CustomUserLoginView.as_view()),
    path('logout/', CustomUserLogoutView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('list/', CustomUserList.as_view()),
]
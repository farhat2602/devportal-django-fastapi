from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Profile, CustomUser
from accounts.serializers import CustomUserSerializer, CompanySerializer, TechnologiesSerializer, BadgesSerializer, \
    ProfileSerializer, CustomUserRegisterSerializer
from accounts.utils import get_tokens_for_user


class CustomUserRegisterView(generics.CreateAPIView):
    serializer_class = CustomUserRegisterSerializer


class CustomUserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserLoginView(APIView):
    def post(self, request):
        if 'email' not in request.data or 'password' not in request.data:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if user is not None and user.is_active:
                login(request, user)
                auth_data = get_tokens_for_user(request.user)
                return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
        return Response({'msg': 'Welcome'}, status=status.HTTP_200_OK)


class CustomUserLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserProfileView(generics.RetrieveUpdateAPIView):
    model = Profile
    serializer_class = ProfileSerializer


class CompanyCreateView(generics.CreateAPIView):
    serializer_class = CompanySerializer


class TechnologyCreateView(generics.CreateAPIView):
    serializer_class = TechnologiesSerializer


class BadgesCreateView(generics.CreateAPIView):
    serializer_class = BadgesSerializer

from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView


class SuperuserLoginAPIView(generics.GenericAPIView):
    authentication_classes = (BasicAuthentication,)
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user and user.is_superuser:
            login(request, user)
            return Response({'detail': 'Superuser logged in successfully'}, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    

class LogoutAPIView(APIView):
    authentication_classes = (BasicAuthentication,)
    def post(self, request, *args, **kwargs):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            logout(request)
            return Response({'detail': 'Superuser logged out successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
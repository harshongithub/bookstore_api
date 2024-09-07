from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken


class Bookviewset(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=username, password=password)
    
    refresh = RefreshToken.for_user(user)
    token = refresh.access_token
    
    return Response({'message': 'User created successfully',
                     'access_token': str(token),
                     'refresh_token': str(refresh)}, status=status.HTTP_201_CREATED)


def home(request):
    return render(request,"home.html")

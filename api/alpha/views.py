from __future__ import unicode_literals

from django.http.response import Http404
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_auth.registration.views import RegisterView

from alpha.serializers import PostSerializer, NotificationSerializer, StudentSerializer, LibrarySerializer

from .models import Post, Notification, Student, Library


class PostView(generics.RetrieveUpdateDestroyAPIView, viewsets.ModelViewSet):
    lookup_field = 'pk'
    serializer_class = PostSerializer
    model = Post

    def get_queryset(self):
        return Post.objects.all()
    
    
class NotificationView(generics.RetrieveUpdateDestroyAPIView, viewsets.ModelViewSet):
    lookup_field = 'pk'
    serializer_class = NotificationSerializer
    model = Notification

    def get_queryset(self):
        return Notification.objects.all()
    
    
class StudentView(generics.RetrieveUpdateDestroyAPIView, viewsets.ModelViewSet):
    lookup_field = 'pk'
    serializer_class = StudentSerializer
    model = Student

    def get_queryset(self):
        return Student.objects.all()

class LibraryView(generics.RetrieveUpdateDestroyAPIView, viewsets.ModelViewSet):
    lookup_field = 'pk'
    serializer_class = LibrarySerializer
    model = Library

    def get_queryset(self):
        return Library.objects.all()


from  .views import PostView, NotificationView, StudentView, LibraryView
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers



api_router = routers.SimpleRouter()
api_router.register(r'alpha/post', PostView ,basename='post')
api_router.register(r'alpha/student', StudentView ,basename='student')
api_router.register(r'alpha/library', LibraryView ,basename='library')
api_router.register(r'alpha/notification', NotificationView ,basename='notification')

urlpatterns = [
    url('', include(api_router.urls)),
]
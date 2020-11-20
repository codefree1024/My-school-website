from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework import permissions

from . import serializers
from .models import Course,Student

def index(request):
    return HttpResponse("<h1> Hello, world. </h1>")

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = serializers.UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = serializers.GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]

class CourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        response = super().destroy(*args, **kwargs)
        response.status_code = status.HTTP_200_OK
        return response
class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
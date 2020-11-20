import json

from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client,TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from school_app.models import Course
from school_app.serializers import CourseSerializer

class CourseViewsetTestCase(TestCase):
    def setUp(self):
        self.user = User(username="mary")
        password = 'pass1234'
        self.user.set_password(password)
        self.user.save()
        self.client = Client()
        logged_in=self.client.login(username="mary",password="pass1234")
    def test_course(self):
        response = self.client.post(reverse("course-list"),data={"info":"test course name"})
        self.marg = response.data["id"]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(reverse("course-detail",kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.delete(reverse("course-detail",kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_courses_list(self):
        response = self.client.get(reverse("course-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
        
        

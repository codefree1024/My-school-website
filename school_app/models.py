from django.db import models

class Course(models.Model):
    info = models.CharField(max_length=100)
    def __str__(self):
        return self.info
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    taken_course = models.ManyToManyField(Course)
    def __str__(self):
        return self.last_name
class Meta:
    unique_together = ('first_name', 'last_name',)

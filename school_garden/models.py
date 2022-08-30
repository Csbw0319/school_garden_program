from django.db import models

# Create your models here.

class School(models.Model):
    school_name = models.CharField(max_length=150)

    def __str__(self):
        return self.school_name

class Volunteer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)




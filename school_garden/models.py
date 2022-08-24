from django.db import models

# Create your models here.
DATES = [
    ('M', 'Monday'),
    ('W', 'Wednesday'),
    ('F', 'Friday')
]


class Volunteer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    school_name = models.CharField(default='Enter School Name', max_length=150)

class School(models.Model):
    school_name = models.CharField(max_length=150)
    date = models.CharField(max_length=1, choices=DATES, default=DATES[0][0])




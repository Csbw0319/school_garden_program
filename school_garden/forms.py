from django import forms
from django.forms import ModelForm
from .models import Volunteer
from .models import School



class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = ['school_name']

    def __str__(self):
        return self.school_name

class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = ['first_name', 'last_name', 'school_name']

    
    
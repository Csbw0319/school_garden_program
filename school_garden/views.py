from http.client import HTTPResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import School
from .models import Volunteer
from .forms import SchoolForm, VolunteerForm
# Create your views here.
def index(request):
    print(request.user)
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def info(request):
    return render(request, 'info.html')

def profile(request):
    return render(request, 'profile.html')

def learnmore(request):
    return render(request, 'learnmore.html')

def create(request):
    all_volunteers = Volunteer.objects.all()
    volunteer_form = VolunteerForm()
    return render(request, 'create.html', {'all': all_volunteers, 'volunteer_form': volunteer_form})


def edit(request):
    return render(request, 'edit.html')

def delete(request):
    return render(request, 'delete.html')

def thankyou(request):
    return render(request, 'thankyou.html')

def detail(request):
    volunteer = Volunteer.objects.get()
    volunteer_form = VolunteerForm()
    return(request, 'detail.html', {
        'volunteer': volunteer, 'volunteer_form': volunteer_form
    })

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
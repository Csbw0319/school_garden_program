from django.shortcuts import render
from django.template import loader
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import School
from .forms import SchoolForm
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
    return render(request, 'create.html')

def edit(request):
    return render(request, 'edit.html')

def delete(request):
    return render(request, 'delete.html')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
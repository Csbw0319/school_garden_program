from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import School, Volunteer
from .forms import VolunteerForm
from django.http import HttpResponseRedirect
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

def learnmore(request):
    return render(request, 'learnmore.html')

def create(request):
    submitted = False
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create?submitted=True')
    else:
        form = VolunteerForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'create.html', {'form': form, 'submitted': submitted})


def update_volunteer(request, volunteer_id):
    volunteer = Volunteer.objects.get(pk=volunteer_id)
    return render(request, 'update_volunteer', {'volunteer': volunteer})

def delete(request):
    return render(request, 'delete.html')

def thankyou(request):
    return render(request, 'thankyou.html')

def volunteer(request):
    volunteer_list = Volunteer.objects.all()
    return render(request, 'accounts/volunteer.html', {'volunteer_list': volunteer_list})


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
    model = Volunteer
    volunteer_list = Volunteer.objects.all()
    
class VolunteerView(TemplateView):
    template_name = 'accounts/volunteer.html'
    model = VolunteerForm  
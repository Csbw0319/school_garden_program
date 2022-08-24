from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("School Garden Program")

def about(request):
    return HttpResponse('About Page')

def profile(request):
    return HttpResponse('Profile Page')

def contact(request):
    return HttpResponse('Contact Page')

def login(request):
    return HttpResponse('Login page')

def info(request):
    return HttpResponse('School Gardens')
from django.shortcuts import render
from django.shortcuts import render
from .models import Project

def home(request):
    projects=Project.objects.all()

    return render(request, 'portfolio/home.html',{'projects':projects})
# Create your views here.

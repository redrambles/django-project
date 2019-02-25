from django.shortcuts import render
from django.http import HttpResponse

# You've already specified to look for templates in the 'templates' folder, inside the settings.py file, so the path is in relation to that

# Create your views here.
def index(request):
  return render(request, 'pages/index.html')

def about(request):
  return render(request, 'pages/about.html')
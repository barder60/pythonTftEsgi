from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .project_models import champion

def index(request):
    return render(request, 'app/index.html')

def json_example(request):
    context = {"categories": [75,25,0,0,0]}
    return render(request, 'app/graphStats.html', context=context)
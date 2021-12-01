from django.shortcuts import render
#from .models import

# Create your views here.

def indexPageView(request) :
    return render(request, 'Opioids/index.html')
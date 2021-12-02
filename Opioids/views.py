from django.shortcuts import render
#from .models import
from Opioids.models import Prescriber
from django.db.models import Q

# Create your views here.

def indexPageView(request) :
    return render(request, 'Opioids/index.html')

def searchPageView(request) :
    if(request.method == 'POST'):
        searchTerm = request.POST['searchValue']

        data = Prescriber.objects.filter(Q(fname__icontains=searchTerm) | Q(lname__icontains=searchTerm))

        context = {
            "prescribers" : data,
        }

        return render(request, 'Opioids/prescribers.html', context)
    else:
        return render(request, 'Opioids/index.html')
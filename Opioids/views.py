from django.shortcuts import render
from .models import Drug, Prescriber
#from .models import
from Opioids.models import Prescriber
from django.db.models import Q

# Create your views here.

def drugsPageView(request) :
    drugs = Drug.objects.all()

    context = {
        "drugs": drugs,
    }

    return render(request, 'Opioids/drugs.html', context)

def prescribersPageView(request) :
    prescribers = Prescriber.objects.all()

    context = {
        "prescribers": prescribers,
    }

    return render(request, 'Opioids/prescribers.html', context)

def prescriberInfoPageView(request, prescriber_id) :
    prescribers = Prescriber.objects.get(id = prescriber_id)

    context = {
        "prescribers": prescribers,
    }
    return render(request, 'Opioids/prescriberinfo.html')

def indexPageView(request) :
    return render(request, 'Opioids/index.html')

def searchPageView(request) :
    if(request.method == 'POST'):
        searchTerm = request.POST['searchValue']    
        print('before query')
        data = Prescriber.objects.filter(Q(fname__icontains=searchTerm) | Q(lname__icontains=searchTerm))
        print(data)
        context = {
            "prescribers" : data,
        }

        return render(request, 'Opioids/prescribersSearch.html', context)
    else:
        return render(request, 'Opioids/index.html')
from django.shortcuts import render
from .models import Drug, Prescriber, Prescriber_Drug
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
    prescribers = Prescriber.objects.all()[:5]

    context = {
        "prescribers": prescribers,
    }

    return render(request, 'Opioids/prescribers.html', context)

def prescriberInfoPageView(request, prescriber_id) :
    prescribers = Prescriber.objects.get(id = prescriber_id)
    prescriber_drug = Prescriber_Drug.objects.filter(prescriber = prescriber_id)
    print(prescriber_drug)

    context = {
        "prescribers": prescribers,
        "prescriber_drug": prescriber_drug
    }
    return render(request, 'Opioids/prescriberinfo.html', context)

def indexPageView(request) :
    return render(request, 'Opioids/index.html')

def searchPageView(request) :
    if(request.method == 'POST'):
        searchTerm = request.POST['searchValue'] 
        # This is getting the value of whatever is in the post form
        option = request.POST['optradio']
        if option == "prescribers" :
            data = Prescriber.objects.filter(Q(fname__icontains=searchTerm) | Q(lname__icontains=searchTerm))
            context = {
                "prescribers" : data,
            }
            return render(request, 'Opioids/prescribers.html', context)
        elif option == "drugs" :
            data = Drug.objects.filter(drugname__icontains=searchTerm)
            context = {
                "drugs" : data,
            }
            return render(request, 'Opioids/drugs.html', context)
        else: 
            data = Drug.objects.filter(drugname__icontains=searchTerm, isopioid = True)
            context = {
                "drugs" : data,
            }
            return render(request, 'Opioids/drugs.html', context)
    else:
        return render(request, 'Opioids/index.html')
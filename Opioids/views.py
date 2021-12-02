from django.shortcuts import render
from .models import pd_drugs, pd_prescriber
#from .models import

# Create your views here.

def drugsPageView(request) :
    drugs = pd_drugs.objects.all()

    context = {
        "drugs": drugs,
    }

    return render(request, 'Opioids/drugs.html', context)

def prescribersPageView(request) :
    prescribers = pd_prescriber.objects.all()

    context = {
        "prescribers": prescribers,
    }

    return render(request, 'Opioids/prescribers.html', context)

def prescriberInfoPageView(request, prescriber_id) :
    prescribers = pd_prescriber.objects.get(id = prescriber_id)

    context = {
        "prescribers": prescribers,
    }
    return render(request, 'Opioids/prescriberinfo.html')

def indexPageView(request) :
    return render(request, 'Opioids/index.html')
from django.shortcuts import render
from .models import Drug, Prescriber, Prescriber_Drug
#from .models import
# from Opioids.models import Prescriber
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def drugsPageView(request) :
    drugs = Drug.objects.all()

    context = {
        "drugs": drugs,
    }

    return render(request, 'Opioids/drugs.html', context)

def prescribersPageView(request) :
    prescriber_list = Prescriber.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(prescriber_list,9)

    try:
        prescribers = paginator.page(page)
    except PageNotAnInteger:
        prescribers = paginator.page(1)
    except EmptyPage:
        prescribers = paginator.page(paginator.num_pages)

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

def createPrescriberPageView(request) :
    return render(request, 'Opioids/createprescriber.html')

def editPrescriberPageView(request, prescriber_id) :
    prescribers = Prescriber.objects.get(id = prescriber_id)

    context = {
        "prescribers": prescribers,
    }
    return render(request, 'Opioids/editprescriber.html', context)

def updatePrescriberPageView(request) :
    if request.method == 'POST':
        prescriber_id = request.POST['prescribers_id']
        prescribers = Prescriber.objects.get(id = prescriber_id)

        prescribers.fname = request.POST['fname']
        prescribers.lname = request.POST['lname']
        prescribers.gender = request.POST['gender']
        prescribers.state = request.POST['state']
        prescribers.opioidprescriber = request.POST['opioidprescriber']
        prescribers.credential = request.POST['credential']
        prescribers.specialty = request.POST['specialty']

        prescribers.save()

    return prescribersPageView(request)

def FAQPageView(request) :
    return render(request, 'Opioids/FAQ.html')

def tableauPageView(request) :
    return render(request, 'Opioids/tableau.html')
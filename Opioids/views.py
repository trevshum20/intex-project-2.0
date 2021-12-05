from django.shortcuts import render
from .models import Drug, Prescriber, Prescriber_Drug, pd_statedata, Specialty
#from .models import
# from Opioids.models import Prescriber
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def drugsPageView(request) :
    # drugs = Drug.objects.all()

    drugs_list = Drug.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(drugs_list,9)

    try:
        drugs = paginator.page(page)
    except PageNotAnInteger:
        drugs = paginator.page(1)
    except EmptyPage:
        drugs = paginator.page(paginator.num_pages)

    context = {
        "drugs": drugs,
    }

    return render(request, 'Opioids/drugs.html', context)

def viewDrugPageView(request, drug_id) :
    drug = Drug.objects.get(id = drug_id)
    top10 = Prescriber_Drug.objects.filter(drug_id = drug_id).order_by('-quantity')[:10]

    context = {
        "drug": drug,
        "top10": top10,
    }

    return render(request, 'Opioids/viewDrug.html', context)

def prescribersPageView(request) :
    prescriber_list = Prescriber.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(prescriber_list,6)

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
    specialties = Specialty.objects.all()
    states = pd_statedata.objects.all()

    context = {
        "specialties": specialties,
        "states": states
    }

    return render(request, 'Opioids/createprescriber.html', context)

def editPrescriberPageView(request, prescriber_id) :
    prescribers = Prescriber.objects.get(id = prescriber_id)
    specialties = Specialty.objects.all()
    states = pd_statedata.objects.all()

    context = {
        "prescribers": prescribers,
        "specialties" : specialties,
        "states" : states
    }
    return render(request, 'Opioids/editprescriber.html', context)

def updatePrescriberPageView(request) :
    if request.method == 'POST':
        prescriber_id = request.POST['prescribers_id']
        prescribers = Prescriber.objects.get(id = prescriber_id)
    
        state = pd_statedata.objects.get(id = request.POST['state'])
        specialty = Specialty.objects.get(id = request.POST['specialty'])
        prescribers.fname = request.POST['fname']
        prescribers.lname = request.POST['lname']
        prescribers.gender = request.POST['gender']
        prescribers.state = state
        canPrescribeOpioids = False
        try:
            if request.POST['opioidprescriber'] == "on" :
                canPrescribeOpioids = True
        except: 
            canPrescribeOpioids = False
        print(canPrescribeOpioids)
        prescribers.isopioidprescriber = canPrescribeOpioids
        prescribers.credential = request.POST['credential']
        prescribers.specialty = specialty

        prescribers.save()

    return prescriberInfoPageView(request, prescriber_id)

def createNewPrescriberPageView(request) :
    if request.method == 'POST':
        prescriber = Prescriber()
        state = pd_statedata.objects.get(id = request.POST['state'])
        specialty = Specialty.objects.get(id = request.POST['specialty'])
        prescriber.fname = request.POST['fname']
        prescriber.lname = request.POST['lname']
        prescriber.gender = request.POST['gender']
        prescriber.state = state

        canPrescribeOpioids = False
        try:
            if request.POST['opioidprescriber'] == "on" :
                canPrescribeOpioids = True
        except: 
            canPrescribeOpioids = False
        print(canPrescribeOpioids)
        prescriber.isopioidprescriber = canPrescribeOpioids
        # If it's not on, set it to false.
        
        prescriber.credential = request.POST['credential']
        prescriber.specialty = specialty

        prescriber.save()
        
        print(prescriber.id)
        return prescriberInfoPageView(request, prescriber.id)
    
    return indexPageView(request)


def FAQPageView(request) :
    return render(request, 'Opioids/FAQ.html')

def tableauPageView(request) :
    return render(request, 'Opioids/tableau.html')

def deletePrescriberPageView(request) :
    if request.method == 'POST':
        prescriber_id = request.POST['prescribers_id']
        prescriberdelete = Prescriber.objects.filter(id = prescriber_id)
        prescriberdelete.delete()
    return prescribersPageView(request)
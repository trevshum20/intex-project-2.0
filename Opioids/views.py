from django.shortcuts import render
from .models import Drug, Prescriber, Prescriber_Drug, pd_statedata, Specialty
#from .models import
# from Opioids.models import Prescriber
from django.db.models import Q, Avg, Count, Min, Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
# from urllib import requests
import requests

# Create your views here.

def drugsPageView(request) :
    # drugs = Drug.objects.all()

    drugs_list = Drug.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(drugs_list,8)

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
    paginator = Paginator(prescriber_list,7)

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
    data = Drug.objects.raw('select pd_drugs.id from pd_drugs where isopioid = true')
    total = Prescriber_Drug.objects.filter(drug_id__in=data).aggregate(Sum('quantity'))

    #drugs = Drug.objects.get(isopioid = True)
    #opioids = Prescriber_Drug.objects.filter(drug_id__in=drugs)




   # drugnames = Drug.objects.raw('select pd_drugs.id, drugname from pd_drugs')
    context = {
        "total" : total.get('quantity__sum'),
        #"drugnames" : opioids
    }
    return render(request, 'Opioids/FAQ.html', context)

def tableauPageView(request) :
    return render(request, 'Opioids/tableau.html')

def doctorPrescriberPageView(request):
    return render(request, 'Opioids/doctors.html')

def deletePrescriberPageView(request) :
    if request.method == 'POST':
        prescriber_id = request.POST['prescribers_id']
        prescriberdelete = Prescriber.objects.filter(id = prescriber_id)
        prescriberdelete.delete()
    return prescribersPageView(request)

def mlPageView(request):
    specialties = Specialty.objects.all()
    states = pd_statedata.objects.all()

    context = {
        "specialties": specialties,
        "states": states
    }

    return render(request, 'Opioids/ml.html', context)

def mlResult(request):
    if request.method == 'POST':
        state = request.POST['state']
        specialty = request.POST['specialty']
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        isopioidprescriber = request.POST['isopioidprescriber']




        url = "https://ussouthcentral.services.azureml.net/workspaces/23e46f91ecd045f4a93e030afdde5eab/services/c972d55920ab47509c96ccca34b544ad/execute?api-version=2.0&details=true"

        payload = json.dumps({
        "Inputs": {
            "input1": {
            "ColumnNames": [
                "Gender",
                "State",
                "Specialty",
                "IsOpioidPrescriber"
            ],
            "Values": [
                [
                gender,
                state,
                specialty,
                isopioidprescriber,
                ]
            ]
            }
        },
        "GlobalParameters": {}
        })
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer AojchwOJyA3Ie0lGxmSLu9Sduy/xTdSjxyT5pN1Q77rRLh6cfcTBc7DbYaWwI6wy2GOG2f3jV1Tgj6GbiaWv3A=='
        }

        #response = requests.request("POST", url, headers=headers, data=payload)
        response = requests.request("POST", url, headers=headers, data=payload)

        json_data = json.loads(response.text)
        prediction = round(float(json_data["Results"]['output1']['value']['Values'][0][0]))

        context = {
            "prediction" : prediction,
            "fname" : fname,
            "lname" : lname,
        }

        return mlResultPageView(request, context)
        

    return render(request, 'Opioids/mlresult.html')

def mlResultPageView(request, context) :
    return render(request, 'Opioids/mlresult.html', context)

def rec(request, prescriber_id, gender, state, specialty, isopioidprescriber, fname, lname):

    prescriber_id = prescriber_id
    gender = gender
    state = state
    specialty = specialty
    isopioidprescriber = isopioidprescriber
    fname = fname
    lname = lname
    


    url = "http://f544458e-008c-411e-8e20-2c359d80f42d.eastus2.azurecontainer.io/score"

    payload = json.dumps({
    "Inputs": {
        "WebServiceInput2": [
        {
            "drugname": "ABILIFY",
            "isopioid": False,
            "avg": 7
        },
        {
            "drugname": "ACETAMINOPHEN.CODEINE",
            "isopioid": True,
            "avg": 6
        },
        {
            "drugname": "ACYCLOVIR",
            "isopioid": False,
            "avg": 2
        }
        ],
        "WebServiceInput3": [
        {
            "prescriber_id": 1992883235,
            "drugname": "LANTUS.SOLOSTAR",
            "quantity": 49
        },
        {
            "prescriber_id": 1942270848,
            "drugname": "LANTUS.SOLOSTAR",
            "quantity": 47
        },
        {
            "prescriber_id": 1891750840,
            "drugname": "LANTUS.SOLOSTAR",
            "quantity": 15
        }
        ],
        "WebServiceInput1": [
        {
            "id": prescriber_id,
            "gender": gender,
            "state_id": state,
            "specialty": specialty,
            "isopioidprescriber": isopioidprescriber,
        },
        ]
    },
    "GlobalParameters": {}
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer Z5D4bus96cKMXYbVlqRv8Bdd1Ock2MBT'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    json_data = json.loads(response.text)
    drugRecs = []
    for results in json_data :
        for output in json_data[results] :
            for recomendation in json_data[results][output][0]:
                drugRecs.append(( json_data[results][output][0][recomendation]))

    context = {
        "drugRecs" : drugRecs,
        "fname" : fname,
        "lname" : lname,
        "prescriber_id" : prescriber_id,
    }
    return recResult(request, context)  

def recResult(request, context) :
    return render(request, 'Opioids/recresults.html', context)






    # context = {
    #     "prescriber_id" : prescriber_id,
    #     "state" : state,
    #     "specialty" : specialty,
    #     "fname" : fname,
    #     "lname" : lname,
    #     "gender": gender,
    #     "isopioidprescriber" : isopioidprescriber,
    # }
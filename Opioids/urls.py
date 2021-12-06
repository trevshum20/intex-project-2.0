from django.urls import path
from .views import indexPageView, drugsPageView, prescribersPageView, prescriberInfoPageView
from .views import searchPageView, createPrescriberPageView, editPrescriberPageView, FAQPageView, tableauPageView, updatePrescriberPageView, createNewPrescriberPageView, viewDrugPageView
from .views import doctorPrescriberPageView, deletePrescriberPageView, mlPageView, mlResult, recResult, rec
urlpatterns = [
    path('delete/', deletePrescriberPageView, name='deletePrescriber'),
    path('edit/<int:prescriber_id>/', editPrescriberPageView, name='editPrescriber'),
    path('create/',createPrescriberPageView, name='createPrescriber'),
    path('createNewPrescriber/', createNewPrescriberPageView, name="createNewPrescriber"),
    path('prescriberinfo/<int:prescriber_id>/', prescriberInfoPageView, name='prescriberInfo'),
    path('prescribers/', prescribersPageView, name='prescribers'),
    path('drugs/', drugsPageView, name='drugs'),
    path('viewDrug/<int:drug_id>/', viewDrugPageView, name="viewDrug"),
    path("search/", searchPageView, name="search"),
    path('faq/', FAQPageView, name="FAQ"),
    path('tableau/', tableauPageView, name="tableau"),
    path('update/', updatePrescriberPageView, name="updatePrescriber"),
    path('doctor/', doctorPrescriberPageView, name="doctors"),
    path('ml/', mlPageView, name="ml"),
    path('mlresult/', mlResult, name="mlresult"),
    path('rec/<int:prescriber_id>/<str:gender>/<str:state>/<str:specialty>/<str:isopioidprescriber>/<str:fname>/<str:lname>/', rec, name="rec"),
    path('recresult/', recResult, name="recresult"),
    path('', indexPageView, name="index"),    
]
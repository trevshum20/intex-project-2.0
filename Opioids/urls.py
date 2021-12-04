from django.urls import path
from .views import indexPageView, drugsPageView, prescribersPageView, prescriberInfoPageView, deletePrescriberPageView
from .views import searchPageView, createPrescriberPageView, editPrescriberPageView, FAQPageView
from .views import tableauPageView, updatePrescriberPageView, createNewPrescriberPageView, viewDrugPageView
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
    path('', indexPageView, name="index"),    
]
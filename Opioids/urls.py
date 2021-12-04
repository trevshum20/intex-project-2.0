from django.urls import path
from .views import indexPageView, drugsPageView, prescribersPageView, prescriberInfoPageView
from .views import searchPageView, createPrescriberPageView, editPrescriberPageView, FAQPageView, tableauPageView, updatePrescriberPageView
urlpatterns = [
    path('edit/<int:prescriber_id>/', editPrescriberPageView, name='editPrescriber'),
    path('create/',createPrescriberPageView, name='createPrescriber'),
    path('prescriberinfo/<int:prescriber_id>/', prescriberInfoPageView, name='prescriberInfo'),
    path('prescribers/', prescribersPageView, name='prescribers'),
    path('drugs/', drugsPageView, name='drugs'),
    path("search/", searchPageView, name="search"),
    path('faq/', FAQPageView, name="FAQ"),
    path('tableau/', tableauPageView, name="tableau"),
    path('update/', updatePrescriberPageView, name="updatePrescriber"),
    path('', indexPageView, name="index"),    
]
from django.urls import path
from .views import indexPageView, drugsPageView, prescribersPageView, prescriberInfoPageView, searchPageView

urlpatterns = [
    path('prescriberinfo/', prescriberInfoPageView, name='prescriberInfo'),
    path('prescribers/', prescribersPageView, name='prescribers'),
    path('drugs/', drugsPageView, name='drugs'),
    path("search/", searchPageView, name="search"),
    path('', indexPageView, name="index"),    
]
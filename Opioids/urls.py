from django.urls import path
<<<<<<< HEAD
from .views import indexPageView, drugsPageView, prescribersPageView, prescriberInfoPageView

urlpatterns = [
    path('prescriberinfo/<int:prescriber_id>/', prescriberInfoPageView, name='prescriberInfo'),
    path('prescribers/', prescribersPageView, name='prescribers'),
    path('drugs/', drugsPageView, name='drugs'),
=======
from .views import indexPageView, searchPageView

urlpatterns = [
    path("search/", searchPageView, name="search"),
>>>>>>> master
    path('', indexPageView, name="index"),
]
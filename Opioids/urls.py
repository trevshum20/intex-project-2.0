from django.urls import path
from .views import indexPageView, drugsPageView, prescribersPageView, prescriberInfoPageView

urlpatterns = [
    path('prescriberinfo/<int:prescriber_id>/', prescriberInfoPageView, name='prescriberInfo'),
    path('prescribers/', prescribersPageView, name='prescribers'),
    path('drugs/', drugsPageView, name='drugs'),
    path('', indexPageView, name="index"),
]
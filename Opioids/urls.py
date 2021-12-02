from django.urls import path
from .views import indexPageView, searchPageView

urlpatterns = [
    path("search/", searchPageView, name="search"),
    path('', indexPageView, name="index"),
]
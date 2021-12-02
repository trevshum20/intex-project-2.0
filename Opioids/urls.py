from django.urls import path
from .views import indexPageView, searchPageView

urlpatterns = [
    path('', indexPageView, name="index"),
    path("search/", searchPageView, name="search")
]
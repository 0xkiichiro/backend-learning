from django.urls import path
from .views import home

urlpatterns = [
    #after localhost /home shoes home page in fscohort app
    path("home/", home)
]
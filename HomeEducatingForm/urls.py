from django.urls import path 
from .views import Step1,Step2,Step3,Location, retrieve_data

urlpatterns=[
    path('stepOne/', Step1),
    path('stepTwo/', Step2),
    path('stepThree/', Step3),
    path('location/', Location),
     path('retrieved/<int:id>/', retrieve_data),
]
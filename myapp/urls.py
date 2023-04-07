from django.urls import path
from .views import firstForm, secondForm, getResult

urlpatterns = [
    path('', firstForm, name='first_form'),
    path('second-form/', secondForm, name='second_form'),
    path('result/<str:form_data>', getResult, name='getResult')
]

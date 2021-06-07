from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('form',views.form,name='form'),
    path('formprocess',views.process,name='process'),
    path('Contactformprocess',views.Contactprocess,name='Contactprocess'),
]
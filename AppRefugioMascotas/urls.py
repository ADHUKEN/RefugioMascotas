from unicodedata import name
from urllib.parse import urlparse
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='Inicio'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerUser, name='register'),
    path('addPet', views.addPet, name='addPet'),
    path('viewPet', views.viewPet, name='viewPet'),
    path('updatePet/<pet_id>', views.updatePet, name='updatePet'),
    path('deletePet/<pet_id>', views.deletePet, name='deletePet'),
    path('viewClient', views.viewClient, name='viewClient'),
    path('deleteClient/<Client_id>', views.deleteClient, name='deleteClient'),
    path('updateProfile/<Profile_id>', views.updateProfile, name='updateProfile'),
    path('adoptionRequest', views.adoptionRequest, name='adoptionRequest'),
    path('viewAdoption', views.viewAdoption, name='viewAdoption'),
    path('deleteAdoption/<Adoption_id>', views.deleteAdoption, name='deleteAdoption'),
    path('updateAdoption/<Adoption_id>', views.updateAdoption, name='updateAdoption'),
]


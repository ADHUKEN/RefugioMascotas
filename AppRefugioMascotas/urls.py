from unicodedata import name
from urllib.parse import urlparse
from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.home, name='Inicio'),
    path('login', views.loginUser, name='login'),
    path('verify', views.verify, name='verify'),
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
    
    #? passsword reset email
    
        # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', authViews.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', authViews.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', authViews.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_confirm.html'), name='password_reset_confirm'),
    
    
    path('password_reset/', authViews.PasswordResetView.as_view(template_name='password_reset/password_reset_form.html'), name='password_reset'),
    
    path('reset/done/', authViews.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
     name='password_reset_complete'),
    
    path('captcha', views.captcha,name='captcha'),
]


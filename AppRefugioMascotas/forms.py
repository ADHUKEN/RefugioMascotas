from dataclasses import fields
import email
from faulthandler import disable
from cv2 import CAP_PVAPI_DECIMATION_2OUTOF16, resize
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model
from matplotlib import widgets
from .models import Pets, User, Adoption
from django.forms import ModelForm
from captcha.fields import CaptchaField

User = get_user_model()

class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2', 'image')
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),

        }
         
class addPetForm(ModelForm):
    class Meta:
        model = Pets
        fields = ('species','name','sex','breed','age','vaccination','illness','feeding','rescue_date','adopter','image','description')
        
        widgets = {
            'species': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'breed': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'vaccination': forms.Textarea(attrs={'class': 'form-control','rows':'3' }),
            'illness': forms.Textarea(attrs={'class': 'form-control','rows':'2' }),
            'feeding': forms.Textarea(attrs={'class': 'form-control','rows':'2' }),
            'rescue_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'adopter': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control','rows':'3', }),
        }
                

class adoptionForm(ModelForm):
    class Meta:
        model = Adoption
        fields = ('user','firstName','lastName','email','phone','age','addreses','Pet','reason','otherPets')
        
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'readonly ': ''}),
            'firstName': forms.TextInput(attrs={'class': 'form-control' }),
            'lastName': forms.TextInput(attrs={'class': 'form-control' }),
            'email': forms.EmailInput(attrs={'class': 'form-control' }),
            'phone': forms.NumberInput(attrs={'class': 'form-control' }),
            'age': forms.NumberInput(attrs={'class': 'form-control' }),
            'addreses': forms.TextInput(attrs={'class': 'form-control' }),
            'Pet': forms.Select(attrs={'class': 'form-control' }),
            'reason': forms.Textarea(attrs={'class': 'form-control','rows':'3' }),
            'otherPets': forms.Textarea(attrs={'class': 'form-control','rows':'3' }),

        }

class captchaform(forms.Form):
    captcha = CaptchaField()

class verifyUser(forms.Form):
    pass
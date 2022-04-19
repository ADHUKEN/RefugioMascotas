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
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2', 'image')
        
class addPetForm(ModelForm):
    class Meta:
        model = Pets
        fields = ('species','name','sex','breed','age','vaccination','illness','feeding','rescue_date','description','adopter','image')
        
        widgets = {
            'rescue_date': forms.DateInput(attrs={'class': '', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control','rows':'3', })
        }
                

class adoptionForm(ModelForm):
    class Meta:
        model = Adoption
        fields = ('user','firstName','lastName','email','phone','age','addreses','Pet','reason','otherPets')
        
        widgets = {
            'user': forms.TextInput(attrs={'class': '', 'readonly ': ''}),
            'firstName': forms.PasswordInput(),

        }

class captchaform(forms.Form):
    captcha = CaptchaField()

class verifyUser(forms.Form):
    number = forms.CharField(label='Code')
    class Meta:
        fields = ('number')
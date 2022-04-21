from contextlib import redirect_stderr
from email import message
from email.policy import default
from genericpath import exists
import django
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout ,get_user_model
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in, user_login_failed
from django.dispatch import receiver

from django.http import HttpResponse
from requests import request
from scipy.misc import face

from .models import Pets, User, Adoption, FailedLogin

from .forms import RegisterUserForm, addPetForm , adoptionForm, captchaform, verifyUser


from .FaceDeteccion.FaceDeteccion  import CAPTURANDO , ENTRENANDO,RECONOCIENDO 
# Create your views here.
User = get_user_model()

def home(request):
    return render(request, 'index.html')

def loginUser( request):
    if request.method == "POST":
        username = request.POST['userTextbox']
        password = request.POST['passwordTextbox']
        user = authenticate(request, username=username, password=password)        
             
        try:
            exist = User.objects.get(username=username)
        except:
            messages.success(request, "Usuario inexistente")
        if user is not None:
            FailedLogin.objects.filter(user = exist).delete()
            request.session['pk'] = user.pk
            # Redirect to a success page.
            
            return redirect('verify')

        else: 
            
            if User.objects.filter(username=username).exists():
                print(username)
                if User.objects.get(username=username).is_active == False:
                    messages.success(request, "usuario bloqueado")
                else:
                    
                    try:
                        failex =FailedLogin.objects.get(user=exist)
                        failex.times += 1
                        failex.save()
                        print(FailedLogin.objects.get(user=exist).times)
                        if FailedLogin.objects.get(user=exist).times >= 6:
                            # three tries or more, disactivate the user
                            exist.is_active = False
                            exist.save()
                        elif FailedLogin.objects.get(user=exist).times == 3:
                            return redirect('captcha')
                    except:
                        FailedLogin.objects.create(user=exist, times = 1)
                        
                    messages.success(request, "Contraseña incorrecta")
    return render(request, 'login.html')
    

def verify(request):
    form = verifyUser(request.POST or None)
    pk = request.session.get('pk')
    print(pk)
    if pk:
        user = User.objects.get(pk= pk)
                
        if form.is_valid():
            ENTRENANDO(user.username)
            RECONOCIENDO()
            login(request,user)
            return redirect('Inicio')
            
    return render(request, 'verifyUser.html', {'form':form,})
    

def logoutUser(request):
    logout(request)
    messages.success(request, "Adiooooos")
    return redirect('Inicio')

def registerUser(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, "registrado")
            login(request,user)
            username = request.user.username
            CAPTURANDO(username)
            return redirect('Inicio')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form':form,})

def captcha(request):
    if request.method == "POST":
        form = captchaform(request.POST)
        if form.is_valid():
            messages.success(request, "Correcto")
            return redirect('login')
        else:
            messages.success(request, "Incorrecto")
    form = captchaform()
    return render(request, 'captcha.html', {'form':form,})


def viewPet(request):
    pet_list = Pets.objects.all()
    return render(request, 'viewpet.html', {'pet_list':pet_list})


def addPet(request):    
    if request.method == "POST":
        form = addPetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Mascota ingresada")
            return redirect('addPet')
    else:
        form = addPetForm()
    return render(request, 'addpet.html', {'form':form})

def updatePet(request, pet_id):
    pet = Pets.objects.get(pk=pet_id)
    form = addPetForm(request.POST or None, request.FILES or None, instance=pet)
    if form.is_valid():
        form.save()
        messages.success(request, "Información actualizada")
        return redirect('viewPet')
    
    return render(request, 'updatepet.html', {'pet':pet, 'form':form})


def deletePet(request, pet_id):
    pet = Pets.objects.get(pk=pet_id)
    pet.delete()
    
    return redirect('viewPet')


def viewClient(request):
    user = request.user
    if user.is_authenticated and user.is_superuser :
        Client_list = User.objects.all()
    else :
        Client_list = User.objects.filter(is_staff=False, is_superuser=False)

    return render(request, 'viewClient.html', {'Client_list':Client_list})



def deleteClient(request, Client_id):
    Client = User.objects.get(pk=Client_id)
    Client.delete()
    return redirect('viewClient')
    
def updateProfile(request, Profile_id):
    Profile = User.objects.get(pk=Profile_id)
    form = RegisterUserForm(request.POST or None, request.FILES or None, instance=Profile)
    if form.is_valid():
        user =form.save()
        login(request,user)
        username = request.user.username
        CAPTURANDO(username)
        messages.success(request, "Información actualizada")
        return redirect('Inicio')
    
    return render(request, 'updateProfile.html', {'Profile':Profile, 'form':form})


def adoptionRequest(request):
    submitted = False
    if request.method == "POST":
        form = adoptionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('adoptionRequest?submitted=True')
    else:
        form = adoptionForm(initial={'user': request.user})
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'adoptionrequest.html', {'form':form, 'submitted':submitted})    

def viewAdoption(request):
    adoption_list = Adoption.objects.all()

    return render(request, 'viewAdoption.html', {'adoption_list':adoption_list})


def deleteAdoption(request, Adoption_id):
    adoption = Adoption.objects.get(pk=Adoption_id)
    adoption.delete()
    return redirect('viewAdoption')

def updateAdoption(request, Adoption_id):
    adoption = Adoption.objects.get(pk=Adoption_id)
    form = adoptionForm(request.POST or None, instance=adoption)
    if form.is_valid():
        form.save()
        messages.success(request, "Información actualizada")
        return redirect('viewAdoption')
    
    return render(request, 'updateAdoption.html', {'adoption':adoption, 'form':form})

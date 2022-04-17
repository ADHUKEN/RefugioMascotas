from tabnanny import verbose
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    CHOICES = (
        ('admin', 'Administrador'),
        ('colab', 'Colaborador'),
        ('client', 'Cliente'),
    )

    role = models.CharField(max_length=300, choices=CHOICES, default='client',)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', verbose_name='Foto de perfil')


class Pets(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    species = models.CharField('Especie', max_length=50)
    name = models.CharField('Nombre', max_length=50)
    sex = models.CharField('Sexo', max_length=20, choices=(
        ('macho', 'Macho'),
        ('hembra', 'Hembra'),
    ))
    breed = models.CharField('Raza', max_length=50)
    age = models.IntegerField('Edad')

    vaccination = models.CharField('Vacunacion', max_length=50)

    illness = models.CharField('Enfermedades', max_length=150)
    feeding = models.CharField('Alimentacion', max_length=150)
    rescue_date = models.DateField('Fecha de Rescate')
    description = models.CharField('Descripcion', max_length=150)

    adopter = models.ForeignKey(User, verbose_name='Adoptante' ,blank=True, null=True, on_delete=models.SET_NULL)
    
    #adopter = models.OneToOneField('Adoptante' , max_length=50)
    image = models.ImageField(default='pet.jpg', upload_to='pet_pics' , verbose_name='Foto')


    def __str__(self):
        return self.name


class Adoption(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    user = models.CharField('Usuario', max_length=150)
    firstName = models.CharField('Nombre', max_length=150)
    lastName = models.CharField('Apellido', max_length=150)
    email = models.EmailField('Email', max_length=150)
    
    phone = models.IntegerField('Número de Telefono')
    age = models.IntegerField('Edad')
    addreses = models.CharField('Direccón', max_length=150)
    Pet = models.OneToOneField(Pets, verbose_name='Mascota' ,blank=False, null=False, on_delete=models.CASCADE)
    reason = models.CharField('Motivo para adoptar', max_length=150)
    otherPets = models.CharField('Otras Mascotas', max_length=150,blank=True)
    
    def __str__(self):
        return self.user
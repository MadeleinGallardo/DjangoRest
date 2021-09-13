from django.db import models
#hacer login con email
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
#Manager
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    '''Manager para perfiles de usuario. Aca van las funciones
    que sirven para manipular los objetos'''
    def create_user(self, email, name, password= None):
        '''Creo un nuevo User Profile'''
        if not email:
            raise ValueError('Usuario debe teenr un email')
        
        #normalizar el email, bajar mayusculas a minusculas
        email = self.normalize_email(email)
        
        user = self.model(email=email, name = name)
        user.set_password(password)
        user.save(using=self._db)

        return user 

    def create_superuser(self, email, name, password = True):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

#modelo de login con email
class UserProfile(AbstractBaseUser, PermissionsMixin):
    '''Modelo base de datos para usuarios en el sistema'''
    email = models.EmailField(max_length= 255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS =['name']

    def get_full_name(self):
        '''Obtener nombre completo'''
        return self.name
    
    def get_short_name(self):
        '''Obtener nombre corto'''
        return self.name

    def __str__(self):
        '''Retornar cadena represetando nuestro usuario'''
        return self.email
    


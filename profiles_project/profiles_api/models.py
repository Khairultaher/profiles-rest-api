from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin 
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
   
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError('user must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email = email, name = name)

        user.set_password(password)
        user.save(using= self._db)

        return user
    
    def create_super_user(self,email,name,password):
        user = self.create_user(email,name,password)

        user.is_super_user = True
        user.is_staff = True
        user.save(using= self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """This class represents user profile inside our system"""

    email = models.EmailField(unique= True)
    name = models.CharField(max_length = 250)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default= False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        """Django use this when it needs to convert object to a string"""
        self.email


from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager
from cloudinary.models import CloudinaryField

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField( unique= True)
    address = models.CharField(max_length= 200, blank= True, null= True)
    phone_number = models.CharField(max_length= 15, blank= True, null= True)
    role = models.CharField(max_length=25, default='Member')
    institute = models.CharField(max_length=200, blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    qualifications = models.TextField(blank=True, null=True)
    experience = models.CharField(max_length=200,blank=True, null=True)
    image= CloudinaryField('image',default='default_for_users_hpwnzn',blank=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
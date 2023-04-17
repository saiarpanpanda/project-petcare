

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User


# petcareapp/models.py

from django.db import models

class DogPatient(models.Model):
    registration_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    gender = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    owner_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


    




class BloodReport(models.Model):
     registration_no = models.CharField(primary_key=True, max_length=100)
     patient_name = models.CharField(max_length=100)
     blood_type = models.CharField(max_length=10)
     hemoglobin_level = models.DecimalField(max_digits=5, decimal_places=2)
     Thyroid = models.CharField(max_length=100)
     LFT = models.CharField(max_length=100)
     Lipid_Profile = models.CharField(max_length=100)
     KFT = models.CharField(max_length=100)
     urine_cultune = models.CharField(max_length=100)
     Anbiotic_Sensitivity_Test = models.CharField(max_length=100)
     Glucose = models.CharField(max_length=100)
     Skin_CULTURE = models.CharField(max_length=100)
     STOOL_TEST = models.CharField(max_length=100)
     PHYSICAL_EXAMINATION_OF_URINE = models.CharField(max_length=100)
     Pancreatic_Enzyymes = models.CharField(max_length=100)
     Inflammation = models.CharField(max_length=100)
     Complete_Blood_Count = models.CharField(max_length=100)
     Blood_Protozoa = models.CharField(max_length=100)
 
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create and save a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Create and save a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'





    
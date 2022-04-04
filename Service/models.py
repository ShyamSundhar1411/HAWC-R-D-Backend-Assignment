from django.db import models
from django_countries.fields import CountryField
from autoslug import AutoSlugField
# Create your models here.
class Hospital(models.Model):
    Hospital_Name = models.CharField(max_length = 200)
    Hospital_Code = models.PositiveIntegerField()
    Location = CountryField()
    slug = AutoSlugField(populate_from ="Hospital_Name",unique = True)
    def __str__(self):
        return str(self.Hospital_Name)+'-'+str(self.Hospital_Code)
class Doctor(models.Model):
    Doctor_Id = models.PositiveBigIntegerField()
    Doctor_Name = models.CharField(max_length = 45)
    Profile_Picture = models.ImageField(upload_to='profile/',blank = True)
    Date_of_Joining = models.DateField()
    Qualification = models.CharField(max_length = 200)
    Specialization = models.CharField(max_length = 300,blank = True)
    slug = AutoSlugField(populate_from = "Doctor_Name",unique = True)
    Hospital = models.ForeignKey(Hospital,on_delete = models.CASCADE)
    def __str__(self):
        return 'Dr. '+str(self.Doctor_Name)+'-'+str(self.Qualification)        
    
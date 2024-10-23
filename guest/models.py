from django.db import models
from adminapp.models import *

# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    
    def _str_(self):
        return self.username
    
class user(models.Model):
    username = models.CharField(max_length=50)
    email_id = models.CharField(max_length=50)
    contact_no = models.BigIntegerField()
    state = models.ForeignKey(state, on_delete=models.CASCADE, null=True, related_name='state')
    district = models.ForeignKey(district, on_delete=models.CASCADE, null=True, related_name='district')
    address = models.TextField()
    proof = models.ImageField(upload_to="images/")
    pincode = models.BigIntegerField()
    imagefile = models.ImageField(upload_to="images/")
    login = models.ForeignKey(login, on_delete=models.CASCADE, null=True, related_name='login')
    register_date = models.DateField()
    
    def _str_(self):
        return self.username
    
class rentholder(models.Model):
    rentholder_name = models.CharField(max_length=50)
    rentholder_email = models.CharField(max_length=50)
    rentholder_contact = models.BigIntegerField()
    rentholder_state = models.ForeignKey(state, on_delete=models.CASCADE, null=True)
    rentholder_district = models.ForeignKey(district, on_delete=models.CASCADE, null=True)
    rentholder_address = models.TextField()
    rentholder_proof = models.ImageField(upload_to="images/")
    rentholder_pincode = models.BigIntegerField()
    rentholder_imagefile = models.ImageField(upload_to="images/")
    rentholder_login = models.ForeignKey(login, on_delete=models.CASCADE, null=True)
    rentholder_registerdate = models.DateField()
    
    def _str_(self):
        return self.rentholder_name
  
    
 

   

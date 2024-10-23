from django.db import models
from adminapp.models import *
from guest.models import *
from rentholder.models import *

# Create your models here.
class booking(models.Model):
    product =  models.ForeignKey(product, on_delete=models.CASCADE, null=True)
    rentholder_id =models.IntegerField()
    from_date = models.DateField()
    to_date =  models.DateField()
    requested_date =  models.DateField()
    bill_id =models.IntegerField()
    login =  models.ForeignKey(login, on_delete=models.CASCADE, null=True)
    booking_status = models.CharField(max_length=50)
    
    def _str_(self):
        return self.product

class bookingmaster(models.Model):
    total_price = models.FloatField()
    rentholder =models.ForeignKey(login, on_delete=models.CASCADE, null=True)
    booking_date =  models.DateField()
    booking_status = models.CharField(max_length=50)
    
    def _str_(self):
        return self.total_price

class payment(models.Model):
    rentholder_id =models.IntegerField()
    payment_date = models.DateField()
    adv_amount =  models.FloatField()
    bal_amount =  models.FloatField()
    bill_no =models.IntegerField()
    login =  models.ForeignKey(login, on_delete=models.CASCADE, null=True)
    payment_status = models.CharField(max_length=50)
    
    def _str_(self):
        return self.rentholder_id


  

    
   

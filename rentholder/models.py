from django.db import models
from adminapp.models import *
from guest.models import *

# Create your models here.
class product(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(categories, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE, null=True)
    product_image = models.ImageField(upload_to="images/")
    description =models.TextField()
    rent_price_perday = models.FloatField()
    remarks = models.CharField(max_length=50)
    login =  models.ForeignKey(login, on_delete=models.CASCADE, null=True)
    product_status = models.CharField(max_length=50)
    
    def _str_(self):
        return self.product_name

    
   
		
		

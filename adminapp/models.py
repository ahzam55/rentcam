from django.db import models

# Create your models here.
class state(models.Model):
    statename = models.CharField(max_length=50)
    
    def _str_(self):
        return self.statename
    
class district(models.Model):
    state = models.ForeignKey(state, on_delete=models.CASCADE, null=True, related_name='states')
    districtname = models.CharField(max_length=50)
   
    def _str_(self):
        return self.state
    
class categories(models.Model):
    categoriesname = models.CharField(max_length=50)
   
    def _str_(self):
        return self.categoriesname
    
class brand(models.Model):
    brand = models.CharField(max_length=50)
   
    def _str_(self):
        return self.brand
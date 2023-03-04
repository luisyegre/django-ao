from django.db import models
# Create your models here.
from .tree import AppoTree  
class AppoinmentManager(models.Manager):
    def as_tree(self):
        data = self.order_by('date').all()
        tree = AppoTree()
        tree.head=data[0]
        for i in range(len(data)):
            if i == 0: continue
            tree.append(data[i]) 
        return tree

class Organization(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)

class Appoinment(models.Model):
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    objects = AppoinmentManager()
    
    def __str__(self):
        return self.first_name + ' ' + str(self.date)

def filter_by_date(data,date): 
    size = len(data)
    
    center = size // 2
    date_int = int(str(date).replace('-',''))
    date_el = int(str(data[center].date).replace('-',''))
    
    if not center and date_el != date_int:
        return None
    
    if date_el == date_int:
        return data[center]
    
    if date_int > date_el:
        return filter_by_date(data[center:size],date)
    else:
        return filter_by_date(data[0:center],date)
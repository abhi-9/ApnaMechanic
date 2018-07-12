from django.db import models

from django.contrib.auth.models import User

class Pincode(models.Model):
    pincode = models.IntegerField(unique=True, blank=False)

class Car(models.Model):
    AUDI = 'AU'
    BMW = 'BW'
    HONDA = 'HD'
    NISSAN = 'NS'
    MAKE_IN_CAR_CHOICES = (
        (AUDI, 'AUDI'),
        (BMW, 'BMW'),
        (HONDA, 'Honda'),
        (NISSAN, 'Nissan'),
    )
    make_in_car = models.CharField(
        max_length=6,
        choices=MAKE_IN_CAR_CHOICES,
        default=None,unique=True
    )
    
    def __str__(self):
        return '%s'% (self.make_in_car) 


class MODEL(models.Model):
    
    MODEL_IN_CAR_CHOICES = (
        ('AUDI', 'A3'),
        ('BMW', 'S2'),
        ('HONDA', 'A2'),
        ('NISSAN', 'G3'),
    )
    
    car = models.ForeignKey(Car, related_name='models',on_delete=models.CASCADE) 
    model_in_car = models.CharField(max_length=10,unique=True,choices=MODEL_IN_CAR_CHOICES)
    
    def __str__(self):
        return '%s'% (self.model_in_car) 




class Services(models.Model):
  #  make = models.ForeignKey(MODEL, related_name='services',on_delete=models.CASCADE)
    repair_maintenance = models.CharField(max_length=10,unique=True)
    diagnostics_inspection = models.CharField(max_length=10,unique=True)
    
    
    
    

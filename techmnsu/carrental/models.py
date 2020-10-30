from django.db import models
from django.contrib.auth.models import User
"""
Author : Jai Behl

"""
# Create your models here.

#Payment Tier table
class Payment_Tiers(models.Model):
    tier_id = models.IntegerField(primary_key=True)
    tier_type = models.CharField(max_length=15)
    tier_discount = models.IntegerField()

#Location Table.
class Location(models.Model):
    location_id = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    zip = models.IntegerField()
    street_address = models.CharField(max_length=15)
    phone_number = models.IntegerField()

#Vehicle Table
class Vehicle(models.Model):
    vehicle_id = models.IntegerField(primary_key=True)
    vehicle_make = models.CharField(max_length=15)
    vehicle_model = models.CharField(max_length=15)
    vehicle_type = models.CharField(max_length=15)
    vehicle_year = models.CharField(max_length=15)
    location_id = models.ForeignKey(Location,on_delete=models.CASCADE)
    tier_id = models.ForeignKey(Payment_Tiers,on_delete=models.CASCADE)

#Rental Record Table
class Rental_record:
    rental_id = models.AutoField(primary_key=True)
    rent_date = models.DateField()
    returned_date = models.DateField()
    vehicle_id = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

#Car avaliability

#New Comment here...


















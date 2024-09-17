from django.db import models





    
    # enumerators for status.
    class = Status(models.Textchoices):
        PENDING = 'pending','pending'
        MISSED = 'missed','missed'
        COLLECTED = 'collected','collected'

    #enumerator for type of garbage.
    class = GarbageType(models.TextChoices):
        ORGANIC = 'organic','organic'
        RECYCLABLE = 'recyclable','recyclable'
        HAZARDOUS = 'hazardous','hazardous'

    #enums for maintenance.
    class MaintenanceStatus(models.TextChoices):
        PENDING = 'pending','pending'
        MISSED = 'missed','missed'
        COLLECTED = 'collected','collected'
        
        
        
    #enum for rental spaces availability
    class AvailabilityStatus(models.TextChoices):
        BOOKED = 'booked','booked'
        AVAILABLE = 'available','available'
        
        
# Create your a garbage collection models
class GarbageCollection(models.Model):
    address = models.CharField(max_lengt=255)
    type_of_garbage =models.CharField(max_length=100, 
                                      choice=GarbageType.choices,
                                      default=GarbageType.ORGANIC)
    
    
    scheduled_date = models.DateField()
    status = models.Charfield(max_length=20,
                              choice=Status.choices,
                              default=Status.PENDING)
    

#creating the model for deliveries

class Delivery(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField():
    delivery_date = models.DateField()
    address = models.CharlField(max_length=255)
    mode_of delivery = CharField(max_lenght=50)
    
#creating the models for utilities
class Utilities(models.Model):
    name = CharField(max_lenght=50)
    service_provider = CharField(max_length=255)
    account_number = IntegerField(max_length=12)
    billing_cycle = CharField(max_length=50)
    
    
    
#creating the models for maintenance.
class Maintenance(models.Model):
    task = CharField(max_length=255)
    sheduled_date = DateField()
    service_provider  = CharFeild(max_length=225)
    status = CharFeild(max_length=20, 
                       choice=MaintenanceStatus.choices,
                       default=Maintenance.PENDING)
    
#Creating models for rental spaces
class RentalSpaces(models.Model):
    name = CharField(max_length=255)
    location = CharField(max_length=255)
    size = FloatField()
    rent_amount =  models.DecimalField(max_digits=10, decimal_places=2)
    availablity = CharField(max_length=20,
                            choice=AvailabilityStatus.choices,
                            default=AvailabilityStatus.AVAILABLE)
    
    
#models for shifting
class Shifting(models.Model):
    person_name = CharField(max_length=100)
    old_location = CharField(max_length=255)
    new_location = CharField(maxl_length=255)
    shifting_date = DateField()
    

#models for warehouses
class WareHouse(models.Model):
    location = models.CharField(max_length=255)
    size = models.FloatField()
    available_space = models.FloatField()
    rental_rate = models.DecimalField(max_digits=10, decimal_places=2)
    
                            

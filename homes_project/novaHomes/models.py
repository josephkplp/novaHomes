from django.db import models

# Create your a garbage collection models


class GarbageCollection(models.Model):
    
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
    item_delivered = models.CharField(max_length=100)
    

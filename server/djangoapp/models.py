from django.db import models
from django.utils.timezone import now
from django.core import serializers 
import uuid
import json


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name=models.CharField(null=False, max_length=200, default="name")
    description=models.CharField(null=False, max_length=500, default="description")

    def __str__(self):
        return "Car make details are:"+self.name+" "+self.description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    carmake=models.ForeignKey(CarMake,on_delete=models.CASCADE)
    dealerId=models.IntegerField()
    name=models.CharField(max_length=50, default="name")
    SEDAN='Sedan'
    SUV='SUV'
    WAGON='WAGON'
    type_choices=[(SEDAN,'Sedan'),(SUV,'SUV'),(WAGON,'WAGON')]
    type=models.CharField(null=False, max_length=20, choices=type_choices, default=SUV)
    year=models.DateField()
    
    def __str__(self):
        return "Car Model details are: Name:" + str(self.name)+" dealerId:" + str(self.dealerId)+" type:"+str(self.type)+" year: "+str(self.year)


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name


# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, name, purchase,review, purchase_date, car_make, car_model, car_year, sentiment, id):
        self.dealership = dealership
        self.name= name
        self.purchase= purchase
        self.review=review
        self.purchase_date=purchase_date
        self.car_make=car_make
        self.car_model=car_model
        self.car_year=year
        self.senti=sentiment
        self.id=id

    def __str__(self):
        return "Dealer review:" +self.review
from django.db import models
from django.utils.timezone import now


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
        return "Car Model details are:"\
            +"Name:"+self.name+" dealerId:"+self.dealerId+" type:"+self.type\
                +" year:"+self.year


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data

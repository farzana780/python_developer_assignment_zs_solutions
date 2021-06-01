from django.db import models

# Create your models here.
class Country(models.Model):
    Name = models.CharField(max_length=255)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Code = models.CharField(max_length=255)

    def __str__(self):
        return self.Name

class State(models.Model):
    Name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, related_name='state', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

class Address(models.Model):
    Name = models.CharField(max_length=255)
    House_number = models.CharField(max_length=255)
    Road_number = models.IntegerField()
    state = models.ForeignKey(State, related_name='address',  on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

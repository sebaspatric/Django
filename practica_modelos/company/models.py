from django.db import models

# Create your models here.

class Salary(models.Model):
    amount = models.IntegerField(blank=False, null=False)
    extra_dec = models.BooleanField(default=False)
    extra_jun = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.amount} - {self.extra_dec} - {self.extra_jun}"
    
class Job(models.Model):
    title = models.CharField(max_length=30, blank=False, null=False)
    description = models.TextField(null=True)
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}" 

class Country(models.Model):
    name = models.CharField(max_length=15, blank=False, null=False)
    country_code = models.CharField(max_length=6, blank=False, null=False)

    def __str__(self):
        return f"{self.name} - {self.country_code}"
    
class Location(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    country_code = models.ForeignKey(Country, on_delete=models.CASCADE)

class Place(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    address = models.CharField(max_length=50, blank=False, null=False)
    zip_code = models.CharField(max_length=5, blank=False, null=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.address} - {self.zip_code}"
    
class Employee(models.Model):
    id_number = models.CharField(max_length=10, blank=False, null=False)
    name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(max_length=30, blank=False, null=False)
    address = models.CharField(max_length=50, blank=False, null=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_number} - {self.name} - {self.last_name}"


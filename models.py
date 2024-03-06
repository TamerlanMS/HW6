from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Child(models.Model):
    parent = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class IceCream(models.Model):
    flavor = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

class IceCreamStand(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    ice_creams = models.ManyToManyField(IceCream)

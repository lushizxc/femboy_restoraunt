from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import ManyToManyField


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()


class FemboyMenu(models.Model):
    name = models.CharField(max_length=100,unique=True)
    dishes_in_menu = ManyToManyField('Dish',related_name='menu',blank=True)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    weight = models.FloatField()

    def __str__(self):
        return f'{self.name} for {self.price}'


class TableOrder(models.Model):
    femboy_menu = models.ForeignKey(FemboyMenu,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    start_time =  models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.femboy_menu.name





# Create your models here.

from django.db import models

# Create your models here.

class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)
    
class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    prince = models.IntegerField()
    
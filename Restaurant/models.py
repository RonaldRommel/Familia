from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    desc=models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200,primary_key=True)
    requests = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    guests = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    

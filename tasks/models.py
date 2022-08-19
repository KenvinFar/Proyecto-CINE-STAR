from operator import truediv
from sys import set_asyncgen_hooks
from django.db import models


# Create your models here.



class usuario (models.Model):
    name = models.CharField(max_length=30);
    address = models.CharField(max_length=10);
    email = models.CharField(max_length=25);
    phone = models.CharField(max_length=10);
    user = models.CharField(max_length=20);
    password = models.CharField(max_length=20);
    
class genre (models.Model):
    description = models.CharField(max_length=25); 
    
class movie (models.Model):
    name_movie = models.CharField(max_length=25);
    gender = models.CharField(max_length=25);
    year = models.IntegerField();
    duration =  models.CharField(max_length=5);
    time = models.IntegerField();
    genre =  models.ForeignKey(genre, on_delete=models.SET_NULL, null=True, blank=False);
    

class room (models.Model):
    name_room = models.CharField(max_length=25)
    total_seats = models.IntegerField();


class reservation(models.Model):
    Nombre = models.CharField(max_length=50);
    language_movie = models.CharField(max_length=25);
    duration = models.CharField(max_length=25);
    seating = models.CharField(max_length=25);
    location = models.CharField(max_length=25);
    usuario = models.ForeignKey(usuario, on_delete=models.SET_NULL, null=True, blank=False);
    movie = models.ForeignKey(movie, on_delete=models.SET_NULL, null=True, blank=False);
    room = models.ForeignKey(room, on_delete=models.SET_NULL, null=True, blank=False);
    
class bill (models.Model):
    date  = models.DateField();
    total = models.FloatField();
    paymentMethod =  models.CharField(max_length=20);
    user = models.ForeignKey(usuario, on_delete=models.SET_NULL, null=True, blank=False);

class invoiceDetail (models.Model):
    quantity = models.IntegerField ();
    bill =models.ForeignKey(bill, on_delete=models.SET_NULL, null=True, blank=False);
    reservation = models.ForeignKey(reservation, on_delete=models.SET_NULL, null=True, blank=False);
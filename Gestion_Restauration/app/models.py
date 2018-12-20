# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class Utilisateur(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="utilisateur_user"
    )

    Telephone = models.IntegerField(unique=True,null=True)
    def __str__(self):
         return "%s %s "%(self.user.first_name,self.user.last_name)



def post_save_receiver(sender, instance, created, **kwargs):
    pass


class Categorie(models.Model):
    Libelle = models.CharField(max_length=30,default='Categorie_No_Name')

    def __str__(self):
        return self.Libelle


class Produit(models.Model):
    Designation = models.CharField(max_length=30,default='Produit_No_Name')
    Prix = models.FloatField(null=True, blank=True, default=None)
    Categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    def __str__(self):
        return self.Designation

class Commande(models.Model):
    Date_Commande = models.DateTimeField(default=timezone.now)
    Ordre = models.IntegerField()
    Montant = models.FloatField()
    Client = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    Produits = models.ManyToManyField(Produit,)
    Valide = models.BooleanField(default=False)

    def __str__(self):
        return "Commande "



class Notification(models.Model):
    Message = models.TextField(max_length=250,blank=True,null=True)
    Date_Notif = models.DateTimeField(default=timezone.now)
    Vue = models.BooleanField(default=False)
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    commande = models.ForeignKey(Commande,on_delete=models.CASCADE)
    def __str__(self):
        return self.Message
    

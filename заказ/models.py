from django.db import models
from клиент.models import Client
from продукт.models import Product

# Create your models here.
class Commande(models.Model):

    STATUT = (('в ожидании','в ожидании'),
              ('не доставлен','не доставлен'),
              ('доставлен','доставлен'))
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    produit = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    statut = models.CharField(max_length=200, null=True,choices= STATUT)
    date_creation = models.DateTimeField(auto_now_add=True,null=True)




from django.db import models
from Clientes.models import Cliente

class MarcaTarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_brand = models.TextField()

    class Meta:
        db_table = 'marca_tarjeta'

class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    customer_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    card_number = models.TextField(unique=True)
    cvv = models.TextField(db_column='CVV')  
    valid_from = models.DateField()
    xpiration_date = models.DateField()
    card_type = models.TextField()
    cardbrand_id = models.ForeignKey(MarcaTarjeta, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tarjeta'
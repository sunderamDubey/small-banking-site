
from django.db import models


class TipoCuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    ac_type = models.TextField()

    class Meta:
        db_table = 'tipo_cuenta'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    account_type = models.ForeignKey(TipoCuenta, models.DO_NOTHING)
    type = models.TextField()

    class Meta:
        db_table = 'cuenta'


class Movimientos(models.Model):
    movement_id = models.AutoField(primary_key=True)
    no_account = models.IntegerField(null=True)
    amount = models.IntegerField()
    type_operation = models.TextField()
    hour = models.CharField(max_length=200)

    class Meta:
        db_table = 'movimientos'

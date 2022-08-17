
from random import choices
from django.db import models


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.CharField(max_length=20, 
    choices = [('PERSONAL', 'PERSONAL'), ('HIPOTECARIO', 'HIPOTECARIO'), ('PRENDARIO', 'PRENDARIO')])
    loan_date = models.DateField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        db_table = 'prestamo'
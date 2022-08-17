
from django.db import models
from django.contrib.auth.models import User


class TipoCliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    cu_type = models.TextField()

    class Meta:
        db_table = 'tipo_cliente'


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()
    customer_dni = models.TextField(db_column='customer_DNI', unique=True)
    dob = models.TextField()
    branch_id = models.IntegerField()
    customer_type = models.ForeignKey(TipoCliente, models.DO_NOTHING)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def approve_loan(self, amount):
        if self.customer_type.cu_type == 'BLACK' and amount <= 500000:
            return True

        if self.customer_type.cu_type == 'GOLD' and amount <= 300000:
            return True

        if self.customer_type.cu_type == 'CLASSIC' and amount <= 100000:
            return True
        return False

    def __str__(self) -> str:
        return f"{self.customer_name}"

    class Meta:
        db_table = 'cliente'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')
    branch_id = models.IntegerField()

    class Meta:
        db_table = 'empleado'

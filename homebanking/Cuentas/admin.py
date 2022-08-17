from django.contrib import admin
from .models import Cuenta


@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ['account_id', 'customer_id', 'balance', 'iban']

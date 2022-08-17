from django.contrib import admin

# Register your models here.
from .models import Cliente


# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'customer_surname', 'customer_name']

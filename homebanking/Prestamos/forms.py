from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Prestamo

#Formulario de prestamo
class LoanForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['loan_type', 'loan_total', 'loan_date']
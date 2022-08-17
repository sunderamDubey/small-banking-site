from http import client
from django.shortcuts import render
from Clientes.models import Cliente
from Cuentas.models import Cuenta
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.views import generic
from .forms import LoanForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
from django.db import connection


@method_decorator(login_required, name='dispatch')
class LoanRequest(generic.CreateView):
    form_class = LoanForm
    success_url = reverse_lazy('prestamos')
    template_name = 'Prestamos/template/Prestamos/prestamos.html'

    def form_valid(self, form):
        user = self.request.user
        cliente = Cliente.objects.get(user_id=user.id)
        hoy = datetime.date(datetime.now())
        currenttime = datetime.now()
        hora = currenttime.strftime('%H:%M:%S')
        diaenform = form.cleaned_data.get('loan_date')
        datacuenta = Cuenta.objects.filter(customer_id=cliente.customer_id)
        cuentapesos = None
        cuentacorri = None

        for c in datacuenta:
            if c.type == 'Caja de ahorro en pesos':
                cuentapesos = c.account_id

        if not cuentapesos:
            for c in datacuenta:
                if c.type == 'Cuenta Corriente':
                    cuentacorri = c.account_id
                    break

        if cuentapesos:
            numerocuenta = cuentapesos
        else:
            numerocuenta = cuentacorri

        montoenform = form.cleaned_data.get('loan_total')
        montoactualizado = montoenform * 100

        def balanceupdate(self, montoactualizado, numerocuenta):
            with connection.cursor() as cursor:
                cursor.execute("UPDATE cuenta SET balance = balance + %s WHERE account_id = %s", [
                               montoactualizado, numerocuenta])

        def movimupdate(self, numerocuenta, montoenform, hora):
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO movimientos(no_account, amount, type_operation, hour) VALUES(%s, %s, 'Préstamo', %s)", [
                               numerocuenta, montoenform, hora])

        if not datacuenta:
            form.add_error(field=None, error='El cliente no posee una cuenta')
            return self.form_invalid(form)

        if not cliente.approve_loan(form.cleaned_data.get('loan_total')):
            form.add_error(field=None, error='Préstamo rechazado')
            return self.form_invalid(form)

        if not diaenform >= hoy:
            form.add_error(field=None, error='La fecha solicitada es inválida')
            return self.form_invalid(form)

        else:
            balanceupdate(self, montoactualizado, numerocuenta)
            movimupdate(self, numerocuenta, montoenform, hora)
            form.instance.customer_id = cliente.customer_id
            super(LoanRequest, self).form_valid(form)

        return render(self.request, 'Prestamos/template/Prestamos/prestamos.html', context={'form': form, 'success_msg': 'Préstamo aprobado', 'cuentapesos': cuentapesos, 'cuentacorri': cuentacorri})

from django.shortcuts import render
from Clientes.models import Cliente
from Cuentas.models import Cuenta
from .models import Tarjeta


def index3 (request):
    datacliente = Cliente.objects.get(user_id = request.user.id)
    try:
        datacuenta = Cuenta.objects.filter(customer_id = datacliente.customer_id)
        largodatacuenta = len(Cuenta.objects.filter(customer_id = datacliente.customer_id))
    except:
        datacuenta = None
    
    if largodatacuenta == 0: 
            datatarjeta = None
    else:
        datatarjeta = []
        for c in datacuenta:
            x = Tarjeta.objects.filter(account_id = c.account_id)
            if x:
                datatarjeta.append(x)

    return render (request, 'Tarjetas/template/Tarjetas/gestiones.html', context={'datacliente':datacliente, 'datacuenta':datacuenta, 'datatarjeta':datatarjeta})
# Generated by Django 4.0.6 on 2022-08-13 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.TextField()),
                ('employee_surname', models.TextField()),
                ('employee_hire_date', models.TextField()),
                ('employee_dni', models.TextField(db_column='employee_DNI')),
                ('branch_id', models.IntegerField()),
            ],
            options={
                'db_table': 'empleado',
            },
        ),
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('cu_type', models.TextField()),
            ],
            options={
                'db_table': 'tipo_cliente',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.TextField()),
                ('customer_surname', models.TextField()),
                ('customer_dni', models.TextField(db_column='customer_DNI', unique=True)),
                ('dob', models.TextField()),
                ('branch_id', models.IntegerField()),
                ('customer_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Clientes.tipocliente')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-15 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prestamos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='loan_date',
            field=models.DateField(),
        ),
    ]
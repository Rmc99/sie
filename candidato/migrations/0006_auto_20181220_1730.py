# Generated by Django 2.1.4 on 2018-12-20 17:30

import cpffield.cpffield
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidato', '0005_auto_20181220_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='cpf',
            field=cpffield.cpffield.CPFField(max_length=14, verbose_name='CPF'),
        ),
    ]

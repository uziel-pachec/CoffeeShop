# Generated by Django 5.1.1 on 2024-10-22 04:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0004_pedido_ventadertalle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido_ventadertalle',
            name='productoAsociado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffee.coffee'),
        ),
    ]
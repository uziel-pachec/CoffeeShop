# Generated by Django 5.1.1 on 2024-10-22 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0005_alter_pedido_ventadertalle_productoasociado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido_ventadertalle',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
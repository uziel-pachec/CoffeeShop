# Generated by Django 5.1.1 on 2024-11-05 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0010_pedido_ventadertalle_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido_ventadertalle',
            name='correo',
        ),
    ]
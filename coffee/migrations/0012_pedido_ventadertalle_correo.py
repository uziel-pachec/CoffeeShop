# Generated by Django 5.1.1 on 2024-11-05 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0011_remove_pedido_ventadertalle_correo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido_ventadertalle',
            name='correo',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]

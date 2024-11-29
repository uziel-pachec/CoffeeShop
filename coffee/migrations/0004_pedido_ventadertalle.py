# Generated by Django 5.1.1 on 2024-10-21 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0003_fondo'),
    ]

    operations = [
        migrations.CreateModel(
            name='pedido_ventaDertalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateField(auto_now=True)),
                ('precioUnitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('productoAsociado', models.CharField(max_length=255)),
            ],
        ),
    ]

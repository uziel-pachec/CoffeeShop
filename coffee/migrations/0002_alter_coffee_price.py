# Generated by Django 5.1.1 on 2024-09-16 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]

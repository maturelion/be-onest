# Generated by Django 3.2.21 on 2023-09-30 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.FloatField(default=0),
        ),
    ]

# Generated by Django 3.2.21 on 2023-09-30 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposits', '0003_auto_20230930_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='tx_hash',
            field=models.CharField(default='', max_length=225),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deposit',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

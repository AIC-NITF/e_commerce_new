# Generated by Django 3.0.8 on 2020-08-12 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ammount',
            field=models.IntegerField(default=0),
        ),
    ]

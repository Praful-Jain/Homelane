# Generated by Django 4.2.7 on 2023-12-14 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_backbonecustomerevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showroom',
            name='supplier_id',
            field=models.IntegerField(unique=True),
        ),
    ]
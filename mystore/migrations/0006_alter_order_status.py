# Generated by Django 4.2.7 on 2023-11-21 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0005_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='New', max_length=5),
        ),
    ]
# Generated by Django 4.2.7 on 2023-11-21 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0003_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

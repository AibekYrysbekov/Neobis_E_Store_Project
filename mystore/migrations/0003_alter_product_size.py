# Generated by Django 4.2.7 on 2023-11-19 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0002_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
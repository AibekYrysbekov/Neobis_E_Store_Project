# Generated by Django 4.2.7 on 2023-11-21 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0006_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
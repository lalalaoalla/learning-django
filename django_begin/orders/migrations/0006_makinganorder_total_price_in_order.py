# Generated by Django 5.0.6 on 2024-07-12 09:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0005_alter_productinbasket_price_one_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="makinganorder",
            name="total_price_in_order",
            field=models.FloatField(default=0),
        ),
    ]

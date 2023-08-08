# Generated by Django 4.2.3 on 2023-08-08 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=1, verbose_name='주문 수량'),
        ),
    ]

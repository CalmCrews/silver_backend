# Generated by Django 4.2.3 on 2023-08-08 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='total',
        ),
    ]
# Generated by Django 4.2.3 on 2023-08-17 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0006_alter_seller_business_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='business_image',
            field=models.URLField(blank=True, null=True, verbose_name='판매자 이미지'),
        ),
    ]

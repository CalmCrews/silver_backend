# Generated by Django 4.2.3 on 2023-07-28 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='', verbose_name='상품 썸네일'),
        ),
        migrations.AddField(
            model_name='product',
            name='video',
            field=models.FileField(blank=True, upload_to='', verbose_name='상품 영상'),
        ),
    ]
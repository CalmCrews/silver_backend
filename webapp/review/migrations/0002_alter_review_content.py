# Generated by Django 4.2.3 on 2023-08-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(blank=True, max_length=101, verbose_name='내용'),
        ),
    ]

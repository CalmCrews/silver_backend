# Generated by Django 4.2.3 on 2023-07-28 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_naverid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='kakaoId',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='카카오 아이디'),
        ),
        migrations.AlterField(
            model_name='user',
            name='naverId',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='네이버 아이디'),
        ),
    ]

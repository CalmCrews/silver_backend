# Generated by Django 4.2.3 on 2023-07-28 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_kakaoid_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='naverId',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='네이버 아이디'),
        ),
    ]

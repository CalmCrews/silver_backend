# Generated by Django 4.2.3 on 2023-08-09 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0008_remove_clubproduct_maximum_remove_userclub_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='tag',
            field=models.CharField(blank=True, verbose_name='모임 태그'),
        ),
        migrations.AlterField(
            model_name='club',
            name='name',
            field=models.CharField(max_length=40, verbose_name='모임명'),
        ),
        migrations.DeleteModel(
            name='ClubTag',
        ),
    ]
# Generated by Django 4.2.3 on 2023-08-09 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0009_club_tag_alter_club_name_delete_clubtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='tag',
            field=models.CharField(verbose_name='모임 태그'),
        ),
    ]

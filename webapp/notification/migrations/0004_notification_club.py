# Generated by Django 4.2.3 on 2023-08-16 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_alter_notification_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='club',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

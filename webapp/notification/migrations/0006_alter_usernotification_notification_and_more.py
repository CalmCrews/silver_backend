# Generated by Django 4.2.3 on 2023-08-16 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notification', '0005_remove_notification_club_remove_notification_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernotification',
            name='notification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_notification', to='notification.notification', verbose_name='알림'),
        ),
        migrations.AlterField(
            model_name='usernotification',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='받는 사람'),
        ),
    ]

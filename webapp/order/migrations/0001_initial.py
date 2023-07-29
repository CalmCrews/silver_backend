# Generated by Django 4.2.3 on 2023-07-29 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0004_alter_productqna_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정 일시')),
                ('quantity', models.IntegerField(blank=True, default=1, verbose_name='주문 수량')),
                ('status', models.CharField(blank=True, choices=[('PREPAYMENT', 'PREPAYMENT'), ('FINALPAYMENT', 'FINALPAYMENT'), ('CANCEL', 'CANCEL')], max_length=255, verbose_name='주문 상태')),
                ('initial_price', models.IntegerField(blank=True, default=0, verbose_name='초기 가격')),
                ('final_price', models.IntegerField(blank=True, null=True, verbose_name='최종 가격')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product', verbose_name='상품')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='구매자')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'order',
            },
        ),
    ]
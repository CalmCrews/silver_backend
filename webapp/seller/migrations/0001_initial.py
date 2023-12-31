# Generated by Django 4.2.3 on 2023-08-08 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정 일시')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='상호명')),
                ('represent', models.IntegerField(verbose_name='대표자명')),
                ('business_number', models.CharField(max_length=60, verbose_name='사업자 번호')),
                ('center_number', models.CharField(max_length=60, verbose_name='고객센터 번호')),
                ('email', models.EmailField(max_length=254, verbose_name='이메일')),
            ],
            options={
                'verbose_name': 'Seller',
                'verbose_name_plural': 'Sellers',
                'db_table': 'seller',
            },
        ),
    ]

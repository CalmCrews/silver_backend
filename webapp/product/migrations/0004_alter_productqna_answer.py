# Generated by Django 4.2.3 on 2023-07-28 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_productanswer_productquestion_productqna'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productqna',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productanswer', verbose_name='답변'),
        ),
    ]
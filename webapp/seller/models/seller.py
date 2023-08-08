from django.db import models

from config.models import BaseModel


class Seller(BaseModel):
    class Meta:
        db_table = 'seller'
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'

    name = models.CharField(
        verbose_name='상호명',
        unique=True,
        max_length=30,
    )

    represent = models.IntegerField(
        verbose_name='대표자명',
    )

    business_number = models.CharField(
        verbose_name='사업자 번호',
        max_length=60
    )

    center_number = models.CharField(
        verbose_name='고객센터 번호',
        max_length=60
    )

    email = models.EmailField(
        verbose_name='이메일',
    )

    def __str__(self):
        return self.name


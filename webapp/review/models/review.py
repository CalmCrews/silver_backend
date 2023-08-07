from django.db import models

from config.models import BaseModel
from order.models import Order


class Review(BaseModel):
    class Meta:
        db_table = 'reviews'
        verbose_name = 'review'
        verbose_name_plural = 'reviews'

    order = models.ForeignKey(
        Order,
        verbose_name='주문',
        on_delete=models.CASCADE,
    )

    content = models.TextField(
        verbose_name='내용',
        null=False,
        blank=True,
        max_length=101,
    )

    rating = models.DecimalField(
        verbose_name='별점',
        max_digits=1,
        decimal_places=1,
        null=False,
        blank=True,
    )

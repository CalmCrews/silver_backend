from django.db import models

from config.models import BaseModel
from product.models import Product
from user.models import User


class ProductQnA(BaseModel):
    class Meta:
        db_table = 'productQnA'
        verbose_name = 'ProductQnA'
        verbose_name_plural = 'ProductQnA'

    user = models.ForeignKey(
        User,
        verbose_name='질문한 사람',
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    product = models.ForeignKey(
        Product,
        verbose_name='상품',
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    question = models.ForeignKey(
        'product.ProductQuestion',
        verbose_name='질문',
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    answer = models.ForeignKey(
        'product.ProductAnswer',
        verbose_name='답변',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

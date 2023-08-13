from django.db import models

from config.models import BaseModel
from user.models import User


class ServiceQnA(BaseModel):
    class Meta:
        db_table = 'ServiceQnA'
        verbose_name = 'ServiceQnA'
        verbose_name_plural = 'ServiceQnA'

    user = models.ForeignKey(
        User,
        verbose_name='질문한 사람',
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

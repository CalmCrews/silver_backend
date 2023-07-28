from django.db import models

from config.models import BaseModel


class ProductAnswer(BaseModel):
    class Meta:
        db_table = 'productAnswer'
        verbose_name = 'ProductAnswer'
        verbose_name_plural = 'ProductAnswers'

    content = models.TextField(
        verbose_name='답변 내용',
        null=False,
        blank=True,
    )

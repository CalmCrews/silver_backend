from django.db import models

from config.models import BaseModel


class ProductQuestion(BaseModel):
    class Meta:
        db_table = 'productQuestion'
        verbose_name = 'ProductQuestion'
        verbose_name_plural = 'ProductQuestions'

    title = models.CharField(
        verbose_name='질문 제목',
        max_length=255,
        null=False,
        blank=True,
    )

    content = models.TextField(
        verbose_name='질문 내용',
        null=False,
        blank=True,
    )

    def __str__(self):
        return self.title

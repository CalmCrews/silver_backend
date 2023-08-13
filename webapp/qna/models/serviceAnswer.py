from django.db import models

from config.models import BaseModel


class ServiceAnswer(BaseModel):
    class Meta:
        db_table = 'ServiceAnswer'
        verbose_name = 'ServiceAnswer'
        verbose_name_plural = 'ServiceAnswers'

    content = models.TextField(
        verbose_name='답변 내용',
        null=False,
        blank=True,
    )

    def __str__(self):
        return self.content[:10]

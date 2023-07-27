from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        verbose_name="생성 일시",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name="수정 일시",
        auto_now=True,
    )

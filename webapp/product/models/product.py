from django.db import models
from django.utils import timezone

from config.models import BaseModel
from order.models import Order

PRODUCT_CATEGORY_CHOICES = (
    ('FASHION', 'FASHION'),
    ('DIGITAL', 'DIGITAL'),
    ('FURNITURE', 'FURNITURE'),
    ('FOOD', 'FOOD'),
    ('ANIMAL', 'ANIMAL'),
    ('SPORTS', 'SPORTS'),
    ('HOBBY', 'HOBBY'),
    ('TRAVEL', 'TRAVEL'),
    ('CROSSBORDER', 'CROSSBORDER'),
    ("GIFTCARD", "GIFTCARD"),
    ('LIFE', 'LIFE'),
)


class Product(BaseModel):
    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    name = models.CharField(
        verbose_name='상품명',
        max_length=255,
        null=False,
        blank=True,
    )

    intro = models.TextField(
        verbose_name='상품 소개',
        null=False,
        blank=True,
    )

    price = models.IntegerField(
        verbose_name='상품 가격',
        null=False,
        blank=True,
    )

    category = models.CharField(
        verbose_name='상품 카테고리',
        max_length=255,
        choices=PRODUCT_CATEGORY_CHOICES,
        null=False,
        blank=True,
    )

    thumbnail = models.ImageField(
        verbose_name='상품 썸네일',
        null=False,
        blank=True,
    )

    video = models.FileField(
        verbose_name='상품 영상',
        null=False,
        blank=True,
    )

    seller = models.CharField(
        verbose_name='판매자',
        max_length=255,
        null=False,
        blank=True,
    )

    end_at = models.DateTimeField(
        verbose_name='판매 종료 일시',
        null=False,
        blank=True,
    )

    @property
    def time_passed(self):
        time_passed = self.end_at > timezone.now()
        if time_passed:
            return False
        return True

    def __str__(self):
        return self.name

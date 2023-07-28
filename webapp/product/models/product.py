from django.db import models

from config.models import BaseModel

PRODUCT_CATEGORY_CHOICES = (
    ('FASHION', 'FASHION'),
    ('DIGITAL', 'DIGITAL'),
    ('FURNITURE', 'FURNITURE'),
    ('FOOD', 'FOOD'),
    ('ANIMAL', 'ANIMAL'),
    ('SPORTS', 'SPORTS'),
    ('HOBBY', 'HOBBY'),
    ('TRAVEL', 'TRAVEL'),
    ('CROSSBORRDER', 'CROSSBORRDER'),
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
    )

    intro = models.TextField(
        verbose_name='상품 소개',
        null=False,
    )

    price = models.IntegerField(
        verbose_name='상품 가격',
        null=False,
    )

    category = models.CharField(
        verbose_name='상품 카테고리',
        max_length=255,
        choices=PRODUCT_CATEGORY_CHOICES,
        null=False,
    )

    seller = models.CharField(
        verbose_name='판매자',
        max_length=255,
        null=False,
    )

    total = models.IntegerField(
        verbose_name='전체 상품 수량',
        null=False,
    )

    end_at = models.DateTimeField(
        verbose_name='판매 종료 일시',
        null=False,
    )

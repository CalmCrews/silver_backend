from django.db import models

from config.models import BaseModel


class ClubProduct(BaseModel):
    class Meta:
        db_table = 'club_product'
        verbose_name = 'ClubProduct'
        verbose_name_plural = 'ClubProducts'

    product = models.ForeignKey(
        'product.Product',
        verbose_name='상품',
        on_delete=models.CASCADE,
        null=False,
    )

    club = models.ForeignKey(
        'club.Club',
        verbose_name='모임',
        on_delete=models.CASCADE,
        null=False,
    )
    maximum = models.PositiveIntegerField(
        verbose_name='최대 구매 수량',
        null=False,
        blank=True,
    )
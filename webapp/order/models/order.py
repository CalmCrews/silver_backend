from django.db import models

from config.models import BaseModel
from user.models import User

ORDER_STATUS = (
    ('PREPAYMENT', 'PREPAYMENT'),
    ('FINALPAYMENT', 'FINALPAYMENT'),
    ('CANCEL', 'CANCEL'),
)


class Order(BaseModel):
    class Meta:
        db_table = 'order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='구매자',
    )

    product = models.ForeignKey(
        'club.ClubProduct',
        verbose_name='주문 상품',
        on_delete=models.SET_NULL,
        null=True,
    )

    quantity = models.IntegerField(
        verbose_name='주문 수량',
        null=False,
        blank=True,
        default=1,
    )

    status = models.CharField(
        verbose_name='주문 상태',
        max_length=255,
        choices=ORDER_STATUS,
        null=False,
        blank=True,
    )

    initial_price = models.IntegerField(
        verbose_name='1개당 초기 가격',
        null=False,
        blank=True,
        default=0,
    )

    final_price = models.IntegerField(
        verbose_name='1개당 최종 가격',
        null=True,
        blank=True,
    )

    @property
    def total_initial_price(self):
        if self.initial_price:
            return int(self.quantity) * int(self.initial_price)
        return 0

    @property
    def total_final_price(self):
        if self.final_price:
            return int(self.quantity) * int(self.final_price)
        return 0

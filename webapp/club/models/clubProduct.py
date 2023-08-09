from django.db import models
from django.db.models import Sum

from config.models import BaseModel
from order.models import Order


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

    @property
    def participant_count(self):
        return Order.objects.filter(product=self).values('user').distinct().count()

    @property
    def quantity_sum(self):
        product_quantity_sum = Order.objects.filter(product=self).aggregate(Sum('quantity'))
        return product_quantity_sum['quantity__sum'] if product_quantity_sum['quantity__sum'] else 0

    @property
    def discount_rate(self):
        discount_rate_by_club_level = {
            0: 0,
            1: 0,
            2: 0.02,
            3: 0.03,
            4: 0.05,
        }
        club_level = int(self.club.level)
        product_quantity_sum = Order.objects.filter(product=self).aggregate(Sum('quantity'))
        order_count = product_quantity_sum['quantity__sum'] if product_quantity_sum['quantity__sum'] else 0

        discount_rate_by_order_quantity_count = self.discount_rate_by_order_count(order_count)
        total_discount_rate = (discount_rate_by_club_level[club_level] + discount_rate_by_order_quantity_count)

        return total_discount_rate

    @property
    def current_price(self):
        discounted_price = int(self.product.price * (1 - self.discount_rate))
        return discounted_price

    def __str__(self):
        return f'{self.product.name}'

    def discount_rate_by_order_count(self, order_count):
        if order_count <= 2:
            return 0
        elif 3 <= order_count <= 10:
            return 0.05
        elif 11 <= order_count <= 20:
            return 0.1
        elif 21 <= order_count <= 30:
            return 0.15
        elif 31 <= order_count <= 50:
            return 0.2
        elif 51 <= order_count <= 100:
            return 0.25
        else:
            return 0.3

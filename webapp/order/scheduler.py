from django.utils import timezone

from order.models import Order
from product.models import Product


def order_close_logic():
    end_products = Product.objects.filter(end_at__lte=timezone.now())
    closed_orders = Order.objects.filter(product__product__in=end_products, status='PREPAYMENT')
    current_time = timezone.now()
    formatted_current_time = str(current_time.strftime('%Y-%m-%d %H:%M:%S'))
    print("------------------ 시작 : " + formatted_current_time + "------------------")
    if closed_orders:
        for order in closed_orders:
            order.status = 'FINALPAYMENT'
            print(str(order.product.product.name) + " 상품의 " + str(order.id) + " 번 주문이 종료되었습니다.")
            print(str(order.user) + " 님의 초기 결제 금액 :" + str(order.total_initial_price) + "원")
            print(str(order.user) + " 님의 최종 결제 금액 :" + str(order.total_final_price) + "원")
            order.user.balance += order.total_initial_price - order.total_final_price
            print(str(order.user) + " 님에게 " + str(order.total_initial_price - order.total_final_price) + "원이 환불되었습니다.")
            print(str(order.user) + " 님의 잔액 :" + str(order.user.balance) + "원")
            print("------------------")
            order.user.save()
            order.save()
    else:
        print("종료된 주문이 없습니다.")
    print("------------------ 종료 " + "------------------")

from django.utils import timezone

from club.models import ClubProduct
from product.models import Product


def levelup_logic():
    end_products = Product.objects.filter(end_at__lte=timezone.now())
    end_club_products = ClubProduct.objects.filter(product__in=end_products, registration=False)
    current_time = timezone.now()
    formatted_current_time = str(current_time.strftime('%Y-%m-%d %H:%M:%S'))
    print("------------------ 시작 : " + formatted_current_time + "------------------")
    if end_club_products:
        for product in end_club_products:
            product.registration = True
            if product.achievement_rate == 100:
                product.club.achievement_count += 1
                print("달성률이 100% 되었습니다.")
                if product.club.achievement_count == 3:
                    product.club.level = 1
                    print("레벨1이 되었습니다.")
                elif product.club.achievement_count == 6:
                    product.club.level = 2
                    print("레벨2가 되었습니다.")
                elif product.club.achievement_count == 9:
                    product.club.level = 3
                    print("레벨3이 되었습니다.")
                elif product.club.achievement_count == 12:
                    product.club.level = 4
                    print("레벨4가 되었습니다.")
                elif product.club.achievement_count == 15:
                    product.club.level = 5
                    print("레벨5가 되었습니다.")
                product.save()
                product.club.save()
            else:
                product.save()
                print("달성률이 100인 상품이 아닙니다.")

    else:
        print("종료된 상품이 없습니다.")
    print("------------------ 종료 " + "------------------")

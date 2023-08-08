from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer
from seller.models import Seller
from seller.serializers.sellerSerializer import SellerSerializer


class SellerRetrieveAPIView(RetrieveAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    lookup_url_kwarg = 'seller_id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        seller_id = self.kwargs.get('seller_id')
        sales = Product.objects.filter(seller=seller_id)
        sales_list = []
        for sale in sales:
            product_data = ProductSerializer(sale).data
            sale_data = {
                'id': product_data['id'],
                'name': product_data['name'],
                'thumbnail': product_data['thumbnail'],
            }
            sales_list.append(sale_data)
        number_of_sales = sales.count()
        res = {
            'data': serializer.data,
            'number_of_sales': number_of_sales,
            'sales_list': sales_list,
        }
        return Response(res)
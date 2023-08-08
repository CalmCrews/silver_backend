from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework.response import Response

from order.models import Order
from review.models import Review
from review.serializers import ReviewSerializer


class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_url_kwarg = 'review_id'

    def perform_create(self, serializer):
        order = self.get_order()
        serializer.save(order=order)

    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"message": "로그인이 필요합니다"}, status=401)
        return super().create(request, *args, **kwargs)

    def get_order(self):
        order_id = self.kwargs.get('order_id')
        order = get_object_or_404(Order, id=order_id)
        return order

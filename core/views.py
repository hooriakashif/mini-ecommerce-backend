from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import Product, Order, OrderItem
from .serializers import ProductSerializer, OrderSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

class OrderCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()

            # Save order items from request
            items_data = request.data.get('items', [])
            for item_data in items_data:
                product_id = item_data.get('product')
                quantity = item_data.get('quantity', 1)
                price_at_time = item_data.get('price_at_time')

                try:
                    product = Product.objects.get(id=product_id)
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        quantity=quantity,
                        price_at_time=price_at_time,
                    )
                except Product.DoesNotExist:
                    pass  # skip if product not found

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import ProductViewSet, OrderCreateView   # ← make sure OrderCreateView is imported

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/orders/create/', OrderCreateView.as_view(), name='order-create'),  # ← this line was missing
]
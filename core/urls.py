from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import ProductViewSet

# Create router
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),          # ← this line makes /api/products/ work
]
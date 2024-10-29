from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'parcels', ParcelViewSet)
router.register(r'delivery_proofs', DeliveryProofViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
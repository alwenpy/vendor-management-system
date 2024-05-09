from django.urls import path, include
from rest_framework import routers
from vendor_management.views import VendorViewSet , PurchaseOrderViewSet
# from vendor_management.views import acknowledge_purchase_order

router = routers.DefaultRouter()
router.register('vendors', VendorViewSet)
router.register('purchase_orders', PurchaseOrderViewSet)    

urlpatterns = [
  path('', include(router.urls)),
    path('api/purchase_orders/<int:pk>/acknowledge/', PurchaseOrderViewSet.as_view({'post': 'acknowledge'}), name='acknowledge_purchase_order'),

]
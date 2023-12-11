from django.urls import path
from .views import PurchaseOrderCreateView, PurchaseOrderDeleteView, PurchaseOrderListView,PurchaseOrderDetailView, PurchaseOrderUpdateView
urlpatterns = [
    
    path('create/purchase_orders/', PurchaseOrderCreateView.as_view(), name='purchase-order-create'),
    path('api/purchase_orders/', PurchaseOrderListView.as_view(), name='purchase-order-list'),
    path('api/purchase_orders/<int:po_number>/', PurchaseOrderDetailView.as_view(), name='purchase-order-detail'),
    path('purchase_orders/<int:po_number>/', PurchaseOrderUpdateView.as_view(), name='purchase-order-update'),
    path('purchase_orders/<int:po_number>/delete/', PurchaseOrderDeleteView.as_view(), name='purchase-order-delete'),
]

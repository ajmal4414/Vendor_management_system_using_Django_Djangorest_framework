from django.urls import path
from .views import RegisterUser, VendorCreateView, VendorDeleteView, VendorListView,VendorDetailView, VendorUpdateView

urlpatterns = [
    path('api/createvendors/', VendorCreateView.as_view(), name='vendor-create'),

    path('api/vendors/', VendorListView.as_view(), name='vendor-list'),
    path('api/vendors/<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('api/vendors/update/<int:id>/', VendorUpdateView.as_view(), name='vendor-update'),
    path('api/vendors/<int:id>/delete/', VendorDeleteView.as_view(), name='vendor-delete'),
    path('register/',RegisterUser.as_view(),name="register")
    
]
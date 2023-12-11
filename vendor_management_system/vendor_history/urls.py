from django.urls import path
from .views import VendorPerformanceView
urlpatterns = [
    path('api/vendors/<int:pk>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
]

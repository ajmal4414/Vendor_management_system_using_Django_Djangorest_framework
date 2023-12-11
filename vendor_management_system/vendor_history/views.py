from django.shortcuts import render
from .models import Vendor
from .serializers import HistoricalPerformanceSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication  import TokenAuthentication
# Create your views here.



class VendorPerformanceView(generics.RetrieveAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = HistoricalPerformanceSerializer

    def retrieve(self, request, *args, **kwargs):
        vendor = self.get_object()
        performance_data = {
            'on_time_delivery_rate': vendor.on_time_delivery_rate,
            'quality_rating_avg': vendor.quality_rating_avg,
            'average_response_time': vendor.average_response_time,
            'fulfillment_rate': vendor.fulfillment_rate,
        }
        return Response(performance_data)

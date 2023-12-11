from django.shortcuts import render
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework .response import Response
# Create your views here.

class PurchaseOrderCreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PurchaseOrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        purchase_order = serializer.save()

        # Add any custom logic after creating a purchase order
        # For example, update vendor performance metrics or send notifications

        headers = self.get_success_headers(serializer.data)
        return Response(PurchaseOrderSerializer(purchase_order).data, status=status.HTTP_201_CREATED, headers=headers)


class PurchaseOrderListView(generics.ListCreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

# class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
#     authentication_classes=[TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = PurchaseOrder.objects.all()
#     serializer_class = PurchaseOrderSerializer


class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PurchaseOrderSerializer
    lookup_field = 'po_number'
    queryset = PurchaseOrder.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        purchase_order = serializer.save()

        # Add any custom logic after updating a purchase order
        # For example, recalculate vendor performance metrics or update related data

        return Response(PurchaseOrderSerializer(purchase_order).data)


class PurchaseOrderUpdateView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_field = 'po_number'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        purchase_order = serializer.save()

        # Add any custom logic after updating a purchase order
        # For example, recalculate vendor performance metrics or update related data

        return Response(PurchaseOrderSerializer(purchase_order).data)


class PurchaseOrderDeleteView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_field = 'po_number'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Add any custom logic before deleting a purchase order
        # For example, revert vendor performance metrics or handle related data

        response = super().destroy(request, *args, **kwargs)

        # Add any additional response data or modifications if needed
        return response

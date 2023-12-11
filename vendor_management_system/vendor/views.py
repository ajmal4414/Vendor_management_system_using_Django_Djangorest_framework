from django.shortcuts import render
from .serializers import VendorSerializer
from .models import Vendor
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from .serializers import UserSerializer

from rest_framework .response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
# Create your views here.


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 401, 'errors': serializer.errors, 'message': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        token_obj, created = Token.objects.get_or_create(user=user)

        return Response({
            'status': 200,
            'payload': serializer.data,
            'token': str(token_obj),
            'message': "Your data is saved"
        }, status=status.HTTP_201_CREATED)


class VendorListView(generics.ListCreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorCreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = VendorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        vendor = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(VendorSerializer(vendor).data, status=status.HTTP_201_CREATED, headers=headers)

class VendorUpdateView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        vendor = serializer.save()

        # Add any custom logic after updating a vendor
        # For example, log the update event or perform additional actions

        return Response(VendorSerializer(vendor).data)


class VendorDeleteView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        response = super().destroy(request, *args, **kwargs)
        return response

from django.shortcuts import render

from rest_framework import viewsets
from addresses.models import Address
from addresses.serializers import AddressSerializer
from addresses.filters import AddressFilter

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filterset_class = AddressFilter


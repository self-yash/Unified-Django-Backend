from django.shortcuts import render
from django.http import JsonResponse
from firebase_config import db
from firebase_admin import firestore
from django.views import decorators
from .serializers import DeviceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['POST'])
def add_device(request):
    serializer = DeviceSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data = serializer.validated_data
    device_id = data["device_id"]
    firestore_data = {
        **data,
        "timestamp": firestore.SERVER_TIMESTAMP
    }

    db.collection("devices").document(device_id).set(firestore_data)

    return Response(
        {"message": "Device added successfully"},
        status=status.HTTP_201_CREATED
    )
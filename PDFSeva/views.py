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
        return Response(
            {
                "error": "Validation failed",
                "details": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    data = serializer.validated_data
    device_id = data["device_id"]
    fcm_token = data["fcm_token"]

    devices_ref = db.collection("devices")

    # matching by device_id
    doc_ref = devices_ref.document(device_id)
    doc_snapshot = doc_ref.get()

    firestore_data = {
        **data,
        "timestamp": firestore.SERVER_TIMESTAMP
    }

    if doc_snapshot.exists:
        # Update existing document by device_id
        doc_ref.update(firestore_data)

        return Response(
            {"message": "Device updated by device_id"},
            status=status.HTTP_200_OK
        )

    # matching by fcm_token
    query = devices_ref.where("fcm_token", "==", fcm_token).limit(1).stream()
    matched_docs = list(query)

    if matched_docs:
        existing_doc = matched_docs[0]
        devices_ref.document(existing_doc.id).update(firestore_data)

        return Response(
            {"message": "Device updated by fcm_token"},
            status=status.HTTP_200_OK
        )

    # new document
    devices_ref.document(device_id).set(firestore_data)

    return Response(
        {"message": "Device created successfully"},
        status=status.HTTP_201_CREATED
    )
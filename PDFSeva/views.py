from django.shortcuts import render
from django.http import JsonResponse
from firebase_config import db
# Create your views here.

def add_user(request):
    data = {
        "name": "Yash",
        "role": "Developer",
        "active": True
    }

    db.collection("users").add(data)

    return JsonResponse({"message": "User added successfully"})

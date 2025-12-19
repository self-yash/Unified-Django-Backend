from django.contrib import admin
from django.urls import path,include
from PDFSeva import views


urlpatterns = [
    path('add_device',views.add_device,name="add_device"),
]

from django.contrib import admin
from django.urls import path,include
from PDFSeva import views


urlpatterns = [
    path('test',views.add_user),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.invoices),
    path('invoices', views.invoices),
]
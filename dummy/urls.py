from django.urls import path

from . import views

urlpatterns = [
    path('', views.invoices),
    path('invoices', views.invoices),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
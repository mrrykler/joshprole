from django.urls import path

from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.invoices),
    path('invoices', views.invoices),
    path('<int:order_num>/',views.detail)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
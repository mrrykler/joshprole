from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from models import *
# Create your views here.

def invoices(request):
    context = {"invoice_list":[i.todict() for i in Invoice.objects.all()]}
    return render(request, 'dummy/invoices.html', context)
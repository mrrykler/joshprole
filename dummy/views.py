from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def invoices(request):
    context = {}
    return render(request, 'dummy/invoices.html', context)
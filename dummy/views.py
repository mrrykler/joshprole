from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from datetime import datetime
# Create your views here.

def invoices(request):
    iv = [i.todict() for i in Invoice.objects.all()]
    for d in iv:
        ds = f"{d['odate']:%Y-%m-%d} {d['slot']:0>2}"
        d["sortdate"]=datetime.strptime(ds,"%Y-%m-%d %H")
        d['slot']=d['sortdate'].strftime("%-I:00%p").lower()
    context = {"invoice_list":sorted(iv,key=lambda x:x['sortdate'])}
    return render(request, 'dummy/invoices.html', context)
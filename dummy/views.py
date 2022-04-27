from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *
from datetime import datetime
import json
# Create your views here.

def invoices(request):
    iv = [i.todict() for i in Invoice.objects.all()]
    for d in iv:
        ds = f"{d['odate']:%Y-%m-%d} {d['slot']:0>2}"
        d["sortdate"]=datetime.strptime(ds,"%Y-%m-%d %H")
    context = {"invoice_list":sorted(iv,key=lambda x:x['sortdate'])}
    return render(request, 'dummy/invoices.html', context)
def detail(request,order_num):
    dv = get_object_or_404(Invoice,id=order_num)
    dv = dv.todict()
    dv['purchase']=json.loads(dv['purchase'])
    context = {"inv":dv}
    return render(request, 'dummy/detail.html', context)
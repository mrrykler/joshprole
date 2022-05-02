from random import random, randint, choices
from decimal import Decimal
import datetime
import json
import re
import os
from requests import get
from bs4 import BeautifulSoup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'joshprole.settings')
import django
django.setup()
from dummy.models import Invoice,Product

PRODUCT_BUFFER = [i.todict() for i in Product.objects.all()]
def genvoice():
    I = []
    for p in PRODUCT_BUFFER:
        p["QTY"] = Decimal(int(B:=randint(1,7)>5)+randint(0,5)*int(B))
        I.append(p)
        if I[-1]['type']=="W" and I[-1]["QTY"]>0:
            I[-1]["QTY"]+=Decimal(f"{random():.2f}")
        I[-1]["QTY"]=float(I[-1]["QTY"])
        if not I[-1]["QTY"]%1:
            I[-1]["QTY"] = int(I[-1]["QTY"])
    I = [p for p in I if p['QTY']>0]
    qty = sum(p['QTY'] for p in I if p['type']=='Q')+sum(1 for p in I if p['type']=='W')
    cost = float(sum(Decimal(f"{p['price']*p['QTY']:.2f}") for p in I))
    td = choices(list(range(3,49)),weights=[300,60,30,10,5,3]+[1]*40)[0]
    rn = lambda : datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-5)))
    while (rn()+datetime.timedelta(hours=td)).hour not in range(8,18):
        td+=1
    dt = rn()+datetime.timedelta(hours=td)
    Invoice.objects.create(cost=cost,odate=dt,purchase=json.dumps(I),slot=dt.hour,itemcount=qty)
    print(Invoice.objects.all().last())
    
def scrape():
    soup = BeautifulSoup(get("http://joshprole.com/dummy").text,'html.parser')
    data = {d.td.text:dict(zip(["date","ci"],[t.text for t in d.find_all('td')[1:]])) for d in soup.find_all('tr')[1:]}
    for k in data:
        data[k]['itemcount'],data[k]['cost'] = re.findall(r"(\d+)/\$(\d+.\d+)",data[k]['ci'])[0]
        del data[k]['ci']
    return data

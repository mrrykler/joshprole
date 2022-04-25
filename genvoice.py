from psycopg2 import connect
from random import random, randint
from decimal import Decimal
import json


def retrieve_products():
    with connect("host=joshprole-db.postgres.database.azure.com dbname=postgres user=mrrykler password=Mr.Ryk73r7955") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM products")
        return [p[1:] for p in cur]
PRODUCT_BUFFER = retrieve_products()
def genvoice():
    I = []
    for p in PRODUCT_BUFFER:
        I.append({"name":p[0],"type":p[1],"price":p[2],"QTY":Decimal(int(B:=randint(1,7)>5)+randint(0,5)*int(B))})
        if I[-1]['type']=="W" and I[-1]["QTY"]>0:
            I[-1]["QTY"]+=Decimal(f"{random():.2f}")
    I = [p for p in I if p['QTY']>0]
    qty = sum(p['QTY'] for p in I if p['type']=='Q')+sum(1 for p in I if p['type']=='W')
    cost = sum(Decimal(f"{p['price']*p['QTY']:.2f}") for p in I)
    return {"cost":cost,"qty":qty,"purchase":I}
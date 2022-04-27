from django.db import models

# Create your models here.

class Invoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    itemcount = models.IntegerField()
    cost = models.FloatField()
    slot = models.IntegerField()
    odate = models.DateField()
    purchase = models.JSONField()
    def todict(self):
        return {"itemcount":self.itemcount,"cost":self.cost,"slot":self.slot,"odate":self.odate,"purchase":self.purchase}
    def __str__(self):
        return str(self.todict())

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=1)
    price = models.FloatField()
    def todict(self):
        return {"name":self.name,"type":self.type,"price":self.price}
    def __str__(self):
        return str(self.todict())
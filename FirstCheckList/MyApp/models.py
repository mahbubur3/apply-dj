from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.CharField(max_length=80)
    quantity = models.IntegerField()

    def __str__(self):
        return "%s" % (self.name)


class OrderInfo(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_placed = models.DateField()
    order_delivered = models.DateField()

    def __str__(self):
        return "%s" % (self.product_name)

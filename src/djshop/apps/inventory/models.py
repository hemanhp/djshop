from django.db import models


# Create your models here.

class StockRecord(models.Model):
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE, related_name='stockrecords')
    sku = models.CharField(max_length=64, null=True, blank=True, unique=True)
    buy_price = models.PositiveBigIntegerField(null=True, blank=True)
    sale_price = models.PositiveBigIntegerField()
    num_stock = models.PositiveIntegerField(default=0)
    threshold_low_stack = models.PositiveIntegerField(null=True, blank=True)



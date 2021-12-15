import datetime

from django.db import models

# Create your models here.

class products(models.Model):
    product_name = models.CharField(max_length=100, verbose_name="product name")
    publisher_name = models.CharField(max_length=200, verbose_name="publisher name")
    rent_status = models.BooleanField(default=False)
    last_rented = models.DateTimeField(auto_now_add=True, verbose_name="last rented")

    def __str__(self):
        return self.product_name






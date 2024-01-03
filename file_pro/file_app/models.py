from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=20)
    product_name = models.CharField(max_length=200)
    product_category = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_expiry_date = models.DateField()
    product_manufacturing_date = models.DateField()
    product_hsn_no = models.CharField(max_length=20)
    product_quantity = models.PositiveIntegerField()


    class Meta:
        ordering = ['product_category']
    

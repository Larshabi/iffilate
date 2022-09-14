from django.db import models
from authentication.models import User, Shop

class Product(models.Model):
    shop = models.ForeignKey(Shop, related_name='products', on_delete=models.CASCADE)
    
    
class Order(models.Model):
    pass
class OrderItem(models.Model):
    pass
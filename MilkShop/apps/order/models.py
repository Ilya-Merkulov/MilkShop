from django.db import models
from djmoney.models.fields import MoneyField
from django.db.models.deletion import CASCADE
from MilkShop.apps.authentication.models import User
from MilkShop.apps.product.models import Product, Item


class OrderStatus(models.Model):
    name = models.CharField(max_length=30)


class ShippingAddress(models.Model):
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)


class Order(models.Model):
    total_price = MoneyField(max_digits=14, decimal_places=2, default_currency='UAH')
    ordered = models.DateTimeField(auto_now_add=True)
    shipped = models.DateTimeField()
    cover_image = cover_image = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='user_in_order')
    order_status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, blank=True, null=True,
                                     related_name='order_status')
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='shipping_address')
    product = models.ManyToManyField(Product, through='OrderProduct')
    item = models.ManyToManyField(Item)


class OrderProduct(models.Model):
    order = models.ForeignKey(Product, on_delete=models.CASCADE)
    product = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()



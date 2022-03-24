from django.db import models
from djmoney.models.fields import MoneyField
from django.db.models.deletion import CASCADE
from MilkShop.apps.authentication.models import User
from MilkShop.apps.filters.models import RawMaterial, Taste, ProductCategory, ProductFilter


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='UAH')
    weight = models.DecimalField(max_digits=16, decimal_places=2)
    fat = models.DecimalField(max_digits=3, decimal_places=1)
    average_rate = models.DecimalField(max_digits=3, decimal_places=1, default='0.0', null=True)
    cover_image = models.TextField(blank=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=True, null=True,
                                         related_name='product_category')
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.SET_NULL, blank=True, null=True,
                                     related_name='raw_material')
    taste = models.ForeignKey(Taste, on_delete=models.SET_NULL, blank=True, null=True,
                              related_name='taste')
    product_filter = models.ManyToManyField(ProductFilter)


class ProductReview(models.Model):
    content = models.TextField(blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    rate = models.DecimalField(max_digits=3, decimal_places=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                             related_name='user_in_productReview')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True,
                                related_name='product_in_productReview')


class Item(models.Model):
    inventory_space_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True,
                                related_name='product_in_item')

from django.db import models


class ProductFilterCategory(models.Model):
    name = models.CharField(max_length=30)


class ProductCategory(models.Model):
    name = models.CharField(max_length=30)
    cover_image = cover_image = models.TextField(blank=True)
    product_filter_category = models.ManyToManyField(ProductFilterCategory)


class ProductFilter(models.Model):
    name = models.CharField(max_length=30)
    product_filter_category = models.ForeignKey(ProductFilterCategory, on_delete=models.SET_NULL, blank=True, null=True,
                                                related_name='product_filter_category')


class RawMaterial(models.Model):
    name = models.CharField(max_length=30)


class Taste(models.Model):
    name = models.CharField(max_length=30)

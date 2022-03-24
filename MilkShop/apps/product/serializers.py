from rest_framework import serializers
from MilkShop.apps.product.models import Product, ProductReview
from MilkShop.apps.authentication.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'weight', 'fat', 'average_rate')

    def create(self, validate_data):
        product = Product(
            name=validate_data['name'],
            description=validate_data['description'],
            price=validate_data['price'],
            weight=validate_data['weight'],
            fat=validate_data['fat'],
            average_rate=validate_data['average_rate']
        )
        product.save()
        return product


class ProductReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = ProductReview
        fields = ('id', 'content', 'created_at', 'rate', 'user', 'product')

    def create(self, validate_data):
        product_review = ProductReview(
            content=validate_data['content'],
            rate=validate_data['rate'],
            user=validate_data['user'],
            product=validate_data['product']
        )
#          return ProductReview.objects.create(**validate_data)

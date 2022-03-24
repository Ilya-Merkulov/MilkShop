from rest_framework import serializers
from MilkShop.MilkShop.apps.order.models import Order, OrderStatus, ShippingAddress

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'email', 'first_name', 'last_name', )


'''
class ItemSerializer(serializers.ModelSerializer):
    category_name = serializers.RelatedField(source='category', read_only=True)

    class Meta:
        model = Item
        fields = ('id', 'name', 'category_name')
'''
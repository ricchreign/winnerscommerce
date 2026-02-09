from rest_framework import serializers
from . models import *

# category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# product serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# Cart serializer
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

# CartProduct serializer
class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = '__all__'

# Order serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

# Checkout serializer
class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        # fields = [
        #     'order_by',
        #     'shipping_address',
        #     'mobile',
        #     'email',
        #     'cart',
        #     'amount',
        #     'subtotal',
        # ]
        fields = ['cart','amount','mobile','shipping_address','subtotal','ref','order_status','payment_completed']
        read_only_fields = ['cart', 'subtotal', 'amount']

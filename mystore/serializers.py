from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'address', 'phone_number']


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        if profile_data:
            UserProfile.objects.create(user=user, **profile_data)
        return user


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ('id', 'products', 'customer_name', 'shipping_address', 'status', 'total_price', 'quantity',
                  'discount')
        read_only_fields = ('total_price', 'status', 'discount')

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        quantity = validated_data.pop('quantity')

        order = Order.objects.create(**validated_data)
        for product_data in products_data:
            order.products.add(product_data)

        order.quantity = quantity
        order.save()

        total_price = order.calculate_total_price()
        order.total_price = total_price
        order.save()

        discounted_price = order.discounted_price()
        order.total_price = discounted_price
        order.save()

        return order




from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    color = models.TextField(max_length=500)
    size = models.DecimalField(max_digits=4, decimal_places=2 )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=20)
    images = models.ManyToManyField('Image', related_name='products', blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.product_name


class Image(models.Model):
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image {self.id}"


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Order(models.Model):
    products = models.ManyToManyField('Product', related_name='orders')
    customer_name = models.ForeignKey(User, on_delete=models.CASCADE)
    shipping_address = models.TextField()
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=5, default='New')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Order {self.id}"

    def calculate_total_price(self):
        total_price = sum(product.price * self.quantity for product in self.products.all())
        return total_price

    def discounted_price(self):
        total_price = self.calculate_total_price()

        discount = Decimal('0')
        if total_price > Decimal('20000'):
            discount = total_price * Decimal('0.2')  # 20% скидка
            discounted_price = total_price - discount
            self.discount = f"20% скидка на сумму {discount}"
        elif total_price > Decimal('10000'):
            discount = total_price * Decimal('0.1')  # 10% скидка
            discounted_price = total_price - discount
            self.discount = f"10% скидка на сумму {discount}"
        else:
            discounted_price = total_price  # Без скидки
            self.discount = "Без скидки"

        return discounted_price

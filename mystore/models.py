from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=255)
    images = models.ManyToManyField('Image', related_name='products')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image {self.id}"


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    products = models.ManyToManyField('Product', related_name='orders')
    customer_name = models.CharField(max_length=255)
    shipping_address = models.TextField()
    status = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id}"

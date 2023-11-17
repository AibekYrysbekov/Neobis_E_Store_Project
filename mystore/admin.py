from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Product, Image, Order, UserProfile, Category


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Order)
admin.site.register(UserProfile)
admin.site.register(Category)


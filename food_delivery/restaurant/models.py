from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Profile(models.Model):
    USER_ROLES = (
        ('owner', 'Owner'),
        ('employee', 'Employee'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLES)
    restaurant = models.ForeignKey('Restaurant', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, related_name='categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Modifier(models.Model):
    name = models.CharField(max_length=100)
    menu_item = models.ForeignKey(MenuItem, related_name='modifiers', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    ORDER_STATUS = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    )
    
    restaurant = models.ForeignKey(Restaurant, related_name='orders', on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default='pending')
    payment_method = models.CharField(max_length=10, choices=(('card', 'Card'), ('cash', 'Cash')))
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} - {self.restaurant.name}"

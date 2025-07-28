from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_super_admin = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, blank=True, null=True)

class Permission(models.Model):
    PAGE_CHOICES = [
        ('products', 'Products List'),
        ('marketing', 'Marketing List'),
        ('orders', 'Order List'),
        ('media', 'Media Plans'),
        ('pricing', 'Offer Pricing SKUs'),
        ('clients', 'Clients'),
        ('suppliers', 'Suppliers'),
        ('support', 'Customer Support'),
        ('sales', 'Sales Reports'),
        ('finance', 'Finance & Accounting')
    ]
    ACCESS_CHOICES = [
        ('view', 'View'),
        ('edit', 'Edit'),
        ('create', 'Create'),
        ('delete', 'Delete')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.CharField(max_length=100, choices=PAGE_CHOICES)
    access = models.CharField(max_length=10, choices=ACCESS_CHOICES)

    class Meta:
        unique_together = ('user', 'page', 'access')
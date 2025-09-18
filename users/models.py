from django.db import models

from utils.common_model import CommonModel

# Django Default Authentication User Model
from django.contrib.auth.models import AbstractUser

# Multiple Inheritance
class User(CommonModel, AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('vendor', 'Vendor'),
        ('customer', 'Customer'),
    )
    role = models.CharField(max_length=8, choices=ROLES, default='customer')
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)


    class Meta:
        db_table = 'auth_user'  # Use the same table name as the default User model
        
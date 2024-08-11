from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES=(
    ('Buyer', 'Buyer'),
    ('Seller', 'Seller')
)
class MyUser(AbstractUser): 
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    role=models.CharField(max_length=150, choices=ROLE_CHOICES, blank=True, null=True)

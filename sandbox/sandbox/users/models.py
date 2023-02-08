from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
class User(AbstractBaseUser):
    username = models.CharField(max_length=50)

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    USERNAME_FIELD = 'username'

    is_free_user = models.BooleanField(default=True)
    is_slot_user = models.BooleanField(default=False)
    is_paid_user = models.BooleanField(default=False)

    slot_amount = models.IntegerField(default=1)
    
class FreeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

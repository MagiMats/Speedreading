from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
class FreeUserManager(BaseUserManager):
    def create_user(self, user_name, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            user_name = user_name,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class FreeUser(AbstractBaseUser):
    user_name = models.CharField(max_length=50)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    book_amount = models.IntegerField(default=1)

    objects = FreeUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email




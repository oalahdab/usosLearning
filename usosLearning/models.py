"""
Database models.
"""

from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50, null=True)
    UserName = models.CharField(max_length=50, null=True)
    BirthDay = models.DateField(null=True)
    Country = models.CharField(max_length=60, null=True)
    PhoneNumber = models.CharField(max_length=20, null=True)
    JobType = models.CharField(max_length=50, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

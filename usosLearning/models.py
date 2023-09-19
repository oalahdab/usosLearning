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

    def create_user(self, EmailAddress, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not EmailAddress:
            raise ValueError('User must have an email address.')
        user = self.model(EmailAddress=self.normalize_email(EmailAddress), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    EmailAddress = models.EmailField(max_length=255, unique=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    UserName = models.CharField(max_length=50)
    BirthDay = models.DateField(null=False)
    Country = models.CharField(max_length=60)
    PhoneNumber = models.CharField(max_length=20)
    JobType = models.CharField(max_length=50)

    objects = UserManager()

    USERNAME_FIELD = 'EmailAddress'

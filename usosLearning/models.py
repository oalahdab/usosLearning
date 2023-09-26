"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        if not password:
            raise ValueError('The password is not provided.')
        
        user = self.model(
            email=self.normalize_email(email),
            
            **extra_fields
            )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        """Create and return a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    id = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50, null=True)
    UserName = models.CharField(max_length=50, null=True, unique=True)
    BirthDay = models.DateField(null=True)
    Country = models.CharField(max_length=60, null=True)
    PhoneNumber = models.CharField(max_length=20, null=True)
    JobType = models.CharField(max_length=50, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

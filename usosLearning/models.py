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
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    id = models.BigAutoField(primary_key=True)
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
    def __str__(self):
        return self.email

class Course(models.Model):
    """Course object"""
    instructor = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField()
    lessonCount = models.CharField(max_length=50)
    subjectId = models.IntegerField()
    imageURL = models.TextField()
    lastUpdate = models.DateTimeField()
    duration = models.TimeField()
    enrollmentCount = models.IntegerField()
    targetAudience = models.CharField(max_length=255)
    videoURL = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    price = models.IntegerField()
    discount = models.IntegerField()
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title


class Instructor(models.Model):
    """Instructor object"""
    fullName = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    imageURL = models.CharField(max_length=255)
    socialMediaLink1 = models.CharField(max_length=255)
    socialMediaLink2 = models.CharField(max_length=255)

    def __str__(self):
        return self.fullName

class Tag(models.Model):
    """Tags for filtering courses"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class UserManager(BaseUserManager):
  """ Define a user manager for the User model with no username field """
  
  use_in_migrations = True

  def _create_user(self, email, password, **extra_fields):
    """ Create and save a user with the given email and password """

    if not email:
      raise ValueError('An email address must be given')
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self.db)
    return user

  def create_user(self, email, password=None, **extra_fields):
    """ Create and save a Regular user with the given email and password """

    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(email, password, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    """ Create and save a superuser with the given email and password """

    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    if extra_fields.get('is_staff') is not True:
      raise ValueError('Superuser must have is_staff as True')
    if extra_fields.get('is_superuser') is not True:
      raise ValueError('Superuser must have is_superuser as True') 

    return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
  username = None
  email = models.EmailField(_('email address'), unique = True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = UserManager()
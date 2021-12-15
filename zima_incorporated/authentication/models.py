import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.timezone import now


# overiding the default user mdoel
class MyAccountManager(BaseUserManager):
    def create_user(self, email, phone_number, name, password):
        if not email:
            raise ValueError("Users must have an email")
        if not phone_number:
            raise ValueError("Users must have a phone number")

        user = self.model(
            # convert to lowercase
            email=self.normalize_email(email),
            username=phone_number
        )
        # user.set_password(password)
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    username = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250, unique=True)
    email = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=100, default="subscriber")
    password = models.CharField(max_length=100, default="")
    last_login = models.DateTimeField(verbose_name='date joined', auto_now_add=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    object = MyAccountManager()

    def __str__(self) -> str:
        return self.email + ", " + self.phone_number

    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



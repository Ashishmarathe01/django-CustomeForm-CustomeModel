from django.db import models
from django.contrib.auth.models import  BaseUserManager, AbstractBaseUser
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username,phone, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username, phone, password=None):

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            phone=phone,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Newuser(AbstractBaseUser):
    email            =models.EmailField(verbose_name="emailk",max_length=60,unique=True)
    username         =models.CharField(max_length=60,unique=True)
    date_joined      =models.DateField(verbose_name='date joned',auto_now_add=True)
    last_login       =models.DateField(verbose_name='last login',auto_now=True)
    is_admin         =models.BooleanField(default=False)
    is_active        =models.BooleanField(default=True)
    is_staff         =models.BooleanField(default=False)
    is_superuser     =models.BooleanField(default=False)
    phone            =models.CharField(max_length=12)


# Create your models here.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']
    objects=MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True
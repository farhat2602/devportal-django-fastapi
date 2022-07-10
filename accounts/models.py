from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from accounts.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(max_length=64, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_company = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Company(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='company_logos/')
    bio = models.CharField(max_length=1024)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        user = CustomUser.objects.get(id=self.user.id)
        user.is_company == True
        user.save()
        super().save(*args, **kwargs)


class Technologies(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Badges(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    knowledge = models.ForeignKey(Technologies, on_delete=models.CASCADE,
                                  related_name='users_knowledge', null=True, blank=True)
    badge = models.ForeignKey(Badges, on_delete=models.CASCADE,
                              related_name='users_badge', null=True, blank=True)
    avatar = models.ImageField(upload_to='profile_avatars/', null=True, blank=True)

    def __str__(self):
        return str(self.user)


from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user


from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        return self.get(email=username) or self.get(phone=username)

    def create_user(self, email=None, name=None, phone=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            is_admin=True,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

# from django.contrib.auth.models import BaseUserManager
#
#
# class CustomUserManager(BaseUserManager):
#     def get_by_natural_key(self, username):
#         return self.get(email=username) or self.get(phone=username)
#
#     def create_user(self, email=None, name=None, phone=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         user = self.model(
#             email=self.normalize_email(email),
#             name=name,
#             phone=phone,
#         )
#
#         user.set_unusable_password()
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, name, phone):
#         user = self.create_user(email, name, phone)
#         user.is_admin = True
#         user.save(using=self._db)
#         return user

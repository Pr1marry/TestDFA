from django.db import models
from django.contrib.auth.models import PermissionsMixin, User
# from django.contrib.auth.base_user import AbstractBaseUser
# from django.utils.translation import gettext_lazy as _


class Galary(models.Model):
    picture = models.ImageField(verbose_name='картинка', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return str(self.author) + str(self.pk)

#
# class User(AbstractBaseUser, PermissionsMixin):
#     created = models.DateTimeField(_('created'), auto_now_add=True)
#     email = models.EmailField(_('email'), unique=True, blank=False)
#     name = models.CharField(_('name'), max_length=30, blank=False)
#     last_name = models.CharField(_('last name'), max_length=100, blank=False)
#     is_active = models.BooleanField(_('active'), default=True)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name', 'last_name', 'birthday']
#
#     class Meta:
#         ordering = ('created',)
#         verbose_name = _('user')
#         verbose_name_plural = _('users')
#
#     def get_full_name(self):
#         """
#         Returns the first_name plus the last_name, with a space in between.
#         """
#         full_name = str(self.first_name) + str(self.last_name)
#         return full_name
#
#     def get_short_name(self):
#         """
#         Returns the short name for the user.
#         """
#         return self.name
from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name='Пользователь'
    )

    name = models.CharField(
        max_length=20,
        default=None,
        blank=False,
        verbose_name="Имя"
    )

    surname = models.CharField(
        max_length=20,
        default=None,
        blank=False,
        verbose_name="Фамилия"
    )



    email = models.EmailField(
        max_length=30,
        unique=True,
        blank=False,
        default=None,
        verbose_name='Имейл'
    )

    def __str__(self):
        return "%s %s" % (self.name, self.surname)
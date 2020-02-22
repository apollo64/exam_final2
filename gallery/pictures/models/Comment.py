from django.db import models

from gallery.accounts.models import Account
from gallery.pictures.models import Picture


class Comment(models.Model):
    text = models.TextField(
        verbose_name="текст коммента",
        max_length=100,
        blank=True,
        default=None
    )

    user = models.ForeignKey(Account,
                             related_name="user",
                             on_delete=models.CASCADE,
                             verbose_name='комменты-пользователи'

                             )

    picture = models.ForeignKey(Picture,
                                related_name="users",
                                on_delete=models.CASCADE,
                                verbose_name="комменты-картинки"
                                )

    mark = models.DecimalField(
        max_digits=1,
        blank=False,
        default=None
    )

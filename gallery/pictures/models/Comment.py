from django.db import models

# from gallery.accounts.models import Account
# from gallery.pictures.models import Picture


class Comment(models.Model):
    text = models.TextField(
        verbose_name="текст коммента",
        max_length=100,
        blank=True,
        default=None
    )

    account = models.ForeignKey('accounts.Account',
                             related_name="comment_user",
                             on_delete=models.CASCADE,
                             verbose_name='комменты-пользователи'

                             )

    picture = models.ForeignKey('pictures.Picture',
                                related_name="picture_user",
                                on_delete=models.CASCADE,
                                verbose_name="комменты-картинки"
                                )

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        blank=False,
        default=None
    )

    date = models.DateField(
        verbose_name="Дата добавления",
        null=True,
        blank=True,
        default=None
    )
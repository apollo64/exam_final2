from django.db import models


class Picture(models.Model):
    account = models.ForeignKey('accounts.Account',
                                related_name='picture_account',
                                on_delete=models.CASCADE,
                                )

    comment = models.ForeignKey('pictures.Comment',
                                related_name='picture_comment',
                                on_delete=models.CASCADE
                                )

    title = models.CharField(
        verbose_name="Заголовок",
        max_length=100,
        blank=False,
        default=None
    )
    average_rating = models.DecimalField(
        verbose_name="Средняя оценка",
        max_digits=3,
        decimal_places=1,
        blank=True,
        default=None,
    )
    date = models.DateField(
        verbose_name="Дата добавления",
        null=True,
        blank=True,
        default=None
    )


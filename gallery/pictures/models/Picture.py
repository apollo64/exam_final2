from django.db import models

# Create your models here.
from gallery.accounts.models import Account


class Picture(models.Model):
    account = models.ForeignKey(Account,
                                related_name='account',
                                on_delete=models.CASCADE,
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
        blank=True,
        default=None,
    )

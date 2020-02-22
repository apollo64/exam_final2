from django.db import models


from gallery.accounts.models import Account

class Comment(models.Model):
    text = models.TextField(
        verbose_name="текст комментаэ",
        max_length= 100,
        blank=True,
        default=None
    )

    user = models.ForeignKey(
        related_name = "user",
        on_delete=models.CASCADE,

    )
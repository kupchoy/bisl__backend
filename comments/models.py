# Django
from django.conf import settings
from django.db import models

# local Django
from common.mixins.model import TimestampMixin


class Comment(TimestampMixin, models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author}: {self.text[:50]}..."

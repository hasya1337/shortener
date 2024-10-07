from django.db import models
from django.utils.crypto import get_random_string


class Link(models.Model):
    original_url = models.URLField("Original URL")
    short_url = models.CharField("Short URL", max_length=10, unique=True, blank=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = get_random_string(6)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.short_url

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"

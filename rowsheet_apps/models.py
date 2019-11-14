from django.db import models
from django.conf import settings

# Create your models here.

class ClientApp(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )

    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)

    creation_timestamp = models.DateTimeField(auto_now_add=True)
    last_changed_timestamp = models.DateTimeField(auto_now=True)
    job_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

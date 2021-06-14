from django.db import models
from core.models import BaseModel


# Create your models here.

class Service(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.CharField(max_length=255, null=True, blank=True)
    icon = models.CharField(max_length=255, null=True, blank=True)
    order = models.IntegerField(default=999)
    chk = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"

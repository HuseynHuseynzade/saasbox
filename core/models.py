from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.

class BaseModel(models.Model):
    cdate = models.DateTimeField(auto_now_add=True)
    udate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("cdate",)
        abstract = True


class Slider(BaseModel):
    heading = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    button_text = models.CharField(max_length=255, null=True, blank=True)
    button_url = models.URLField(null=True, blank=True)
    order = models.IntegerField(default=999)

    def __str__(self):
        return f"{self.heading}"


class Feature(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    heading = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    percent_desc = models.CharField(max_length=255, null=True, blank=True)
    percent = models.IntegerField()
    order = models.IntegerField(default=999)
    image = models.ImageField(blank=True, upload_to='uploads')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(500, 350)],
                                     format='JPEG',
                                     options={'quality': 60})

    def get_image(self):
        if self.image_thumbnail:
            return self.image_thumbnail.url
        else:
            return 'static/no_img.png'

    def __str__(self):
        return f"{self.title}"

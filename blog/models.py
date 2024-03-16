from django.db import models
from django.utils import timezone
# Create your models here.

class Article(models.Model):
    STATUS_CHOICES = (
    ('d', 'پیش نویس'),
    ('p', 'منتشر شده'),
    )
    title = models.CharField(max_length= 200, verbose_name = "عنوان مقاله")
    slug = models.SlugField (max_length = 100, unique=True, verbose_name = "آدرس مقاله")
    description = models.TextField (verbose_name = "محتوا")
    thumbnail = models.ImageField (upload_to="images", verbose_name = " تصویر")
    publish = models.DateTimeField (default = timezone.now, verbose_name = "زمان انتشار")
    created = models.DateTimeField (auto_now_add = True, verbose_name = "زمان ساخت")
    updated = models.DateTimeField (auto_now = True)
    status = models.CharField (max_length = 1, choices = STATUS_CHOICES, verbose_name = "وضعیت")
    class Meta(object):
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله ها"


    def __str__(self):
        return self.title

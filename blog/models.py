from django.db import models
from django.utils import timezone
from extentions.utils import jalali_convertor

#my managers
class ArticleManager(models.Manager):
    def published (self):
        return self.filter(status = 'p')

class category(models.Model):
    title = models.CharField(max_length= 200, verbose_name = "عنوان دسته‌بندی")
    slug = models.SlugField (max_length = 100, unique=True, verbose_name = "آدرس دسته‌بندی")
    status = models.BooleanField(default = True, verbose_name = "آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name = "پوزیشن")

    class Meta(object):
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی ها"
        ordering = ['position']

    def __str__(self):
        return self.title


class Article(models.Model):
    STATUS_CHOICES = (
    ('d', 'پیش نویس'),
    ('p', 'منتشر شده'),
    )
    title = models.CharField(max_length= 200, verbose_name = "عنوان مقاله")
    slug = models.SlugField (max_length = 100, unique=True, verbose_name = "آدرس مقاله")
    #category class should be above this class.
    category = models.ManyToManyField(category, verbose_name = "دسته‌بندی", related_name = "articles")
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

    def jpublish(self):
        return jalali_convertor(self.publish)
    jpublish.short_description = "زمان انتشار"

    def category_published(self):
        return self.category.filter(status = True)

    objects = ArticleManager()

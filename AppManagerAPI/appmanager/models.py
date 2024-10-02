from django.db import models
from django.utils import timezone

# مدل برای دسته‌بندی‌ها
class Category(models.Model):
    title = models.CharField(max_length=100)
    icon = models.URLField(max_length=500, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


# مدل برای اپلیکیشن‌ها
class Application(models.Model):
    cat_Id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='applications', null=True, blank=True)  # استفاده از رابطه خارجی
    title = models.CharField(max_length=255)
    packageName = models.CharField(max_length=255)
    versionCode = models.IntegerField()
    versionName = models.CharField(max_length=100)
    Icon = models.URLField(max_length=500, null=True, blank=True)
    shortDescription = models.TextField(null=True, blank=True)
    fullDescription = models.TextField(null=True, blank=True)
    price = models.CharField(max_length=50, null=True, blank=True)
    rate = models.FloatField(null=True, blank=True)
    downloadLink = models.URLField(max_length=500)
    number_installs = models.CharField(max_length=100, null=True, blank=True)
    minSDK = models.IntegerField(null=True, blank=True)
    bulk = models.CharField(max_length=50, null=True, blank=True)
    developer = models.IntegerField(null=True, blank=True)
    IsAnnouncement = models.BooleanField(default=False)
    announcementUrl = models.URLField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)  # اضافه کردن فیلد created_at

    def __str__(self):
        return self.title


# مدل برای اعلان‌ها
class Announcement(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

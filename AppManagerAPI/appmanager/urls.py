from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApplicationViewSet, AnnouncementViewSet, CategoryViewSet

# ایجاد یک DefaultRouter برای مدیریت خودکار مسیرهای API
router = DefaultRouter()

# ثبت ViewSet های مربوط به Application, Announcement و Category
router.register(r'applications', ApplicationViewSet)
router.register(r'announcements', AnnouncementViewSet)
router.register(r'categories', CategoryViewSet)

# تعریف urlpatterns برای شامل کردن مسیرهای API
urlpatterns = [
    path('api/', include(router.urls)),  # قرار دادن تمام مسیرهای API تحت مسیر api/
]

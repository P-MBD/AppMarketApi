from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appmanager.urls')),  # اضافه کردن مسیر اپلیکیشن appmanager
]

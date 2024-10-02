from rest_framework import serializers
from .models import Application, Announcement, Category

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'title', 'packageName', 'versionCode', 'versionName', 
                  'Icon', 'shortDescription', 'fullDescription', 'price', 
                  'rate', 'downloadLink', 'number_installs', 'minSDK', 
                  'bulk', 'developer', 'IsAnnouncement', 'announcementUrl', 
                  'created_at']


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'title', 'message', 'created_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

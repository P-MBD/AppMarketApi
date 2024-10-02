from django.core.management.base import BaseCommand
from appmanager.models import Category, Application, Announcement

class Command(BaseCommand):
    help = 'Create sample data for the application'

    def handle(self, *args, **kwargs):
        # ایجاد دسته‌بندی‌های نمونه
        category1 = Category.objects.create(
            title='Utilities',
            icon='https://example.com/icon_utilities.png',
            description='Applications that help with productivity and efficiency.'
        )
        
        category2 = Category.objects.create(
            title='Games',
            icon='https://example.com/icon_games.png',
            description='Fun and entertaining games.'
        )

        # ایجاد اپلیکیشن‌های نمونه
        app1 = Application.objects.create(
            cat_Id=category1,
            title='Sample Utility App',
            packageName='com.example.sampleutilityapp',
            versionCode=1,
            versionName='1.0',
            Icon='https://example.com/icon_sample_utility.png',
            shortDescription='A sample utility application.',
            fullDescription='This application helps you manage your tasks efficiently.',
            price='Free',
            rate=4.5,
            downloadLink='https://example.com/download/sample_utility_app',
            number_installs='1000+',
            minSDK=21,
            bulk='Free',
            developer=1,
            IsAnnouncement=False,
            announcementUrl=None
        )

        app2 = Application.objects.create(
            cat_Id=category2,
            title='Fun Game',
            packageName='com.example.fungame',
            versionCode=2,
            versionName='1.1',
            Icon='https://example.com/icon_fun_game.png',
            shortDescription='A fun game to play with friends.',
            fullDescription='Enjoy this fun game with your friends and family.',
            price='1.99',
            rate=4.8,
            downloadLink='https://example.com/download/fun_game',
            number_installs='5000+',
            minSDK=19,
            bulk='Paid',
            developer=2,
            IsAnnouncement=True,
            announcementUrl='https://example.com/announcements/fun_game'
        )

        # ایجاد اعلان‌های نمونه
        announcement1 = Announcement.objects.create(
            title='New App Release!',
            message='We have released a new version of the Sample Utility App. Check it out!',
        )

        self.stdout.write(self.style.SUCCESS('Sample data created successfully.'))

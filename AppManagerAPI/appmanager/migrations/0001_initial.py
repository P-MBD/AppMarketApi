# Generated by Django 5.1.1 on 2024-10-02 07:49

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Announcement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("icon", models.URLField(blank=True, max_length=500, null=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Application",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("packageName", models.CharField(max_length=255)),
                ("versionCode", models.IntegerField()),
                ("versionName", models.CharField(max_length=100)),
                ("Icon", models.URLField(blank=True, max_length=500, null=True)),
                ("shortDescription", models.TextField(blank=True, null=True)),
                ("fullDescription", models.TextField(blank=True, null=True)),
                ("price", models.CharField(blank=True, max_length=50, null=True)),
                ("rate", models.FloatField(blank=True, null=True)),
                ("downloadLink", models.URLField(max_length=500)),
                (
                    "number_installs",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("minSDK", models.IntegerField(blank=True, null=True)),
                ("bulk", models.CharField(blank=True, max_length=50, null=True)),
                ("developer", models.IntegerField(blank=True, null=True)),
                ("IsAnnouncement", models.BooleanField(default=False)),
                (
                    "announcementUrl",
                    models.URLField(blank=True, max_length=500, null=True),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "cat_Id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="appmanager.category",
                    ),
                ),
            ],
        ),
    ]

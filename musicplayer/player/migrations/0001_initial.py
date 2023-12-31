# Generated by Django 5.0 on 2023-12-10 23:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('artist', models.CharField(blank=True, max_length=255)),
                ('file', models.FileField(upload_to='media')),
                ('DJ', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mix', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

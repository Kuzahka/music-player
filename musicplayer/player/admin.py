from django.contrib import admin
from .models import Song


class SongAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('title', 'artist')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате


admin.site.register(Song, SongAdmin)
# Register your models here.

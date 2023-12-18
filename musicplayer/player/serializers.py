from rest_framework import serializers

from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        # В прошлом уроке fields = '__all__' изменили на:
        fields = ('title', 'artist', 'DJ')
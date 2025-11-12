from rest_framework import serializers
from django.utils import timezone
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    is_upcoming = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__' 
        read_only_fields = ['organizer']

    def get_is_upcoming(self, obj):
        return obj.start_time > timezone.now()

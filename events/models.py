import uuid
from django.db import models
from cloudinary.models import CloudinaryField
from users.models import CustomUser 


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('event_image',default='default_for_cover_r4fftg', blank=True, null=True)
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    registration_link = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organizer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='events')


    class Meta:
        ordering = ['-start_time']
    

    def __str__(self):
        return self.title 
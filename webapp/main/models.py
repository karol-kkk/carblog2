from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Avatar(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to="images/avatars")

class Event(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Round(models.Model):
    event = models.ForeignKey(Event, related_name='rounds', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()        
    image = models.ImageField(upload_to='round_images/')
    link = models.URLField()

    def __str__(self):
        return f"{self.event.title} - {self.title}"
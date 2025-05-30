from django.db import models


# Create your models here.
class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=255)
    website = models.URLField()

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    platform = models.ForeignKey(
        StreamPlatform, on_delete=models.CASCADE, related_name="watchlist"
    )
    # related_name allows you to access the watchlist from the StreamPlatform instance
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

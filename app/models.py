from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


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


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    description = models.CharField(max_length=255, null=True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(
        "app.WatchList", on_delete=models.CASCADE, related_name="reviews"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review for {self.watchlist.title} - {self.rating} stars"

from django.urls import path, include
from app.api.views import (
    WatchListAV,
    StreamPlatformAV,
    WatchDetailAV,
    StreamPlatformDetailAV,
)

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="Watch-list"),
    path("<int:pk>/", WatchDetailAV.as_view(), name="Watch-Detail"),
    path("stream/", StreamPlatformAV.as_view(), name="Stream-Platform"),
    path(
        "stream/<int:pk>/",
        StreamPlatformDetailAV.as_view(),
        name="Stream-Platform-Detail",
    ),
    # You can add more paths here if needed
]

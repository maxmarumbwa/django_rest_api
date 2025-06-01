from django.urls import path, include
from app.api.views import (
    WatchListAV,
    StreamPlatformAV,
    WatchDetailAV,
    StreamPlatformDetailAV,
)

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="watch-list"),
    path("<int:pk>/", WatchDetailAV.as_view(), name="watch-detail"),
    path("stream/", StreamPlatformAV.as_view(), name="stream-platform"),
    path(
        "stream/<int:pk>/",
        StreamPlatformDetailAV.as_view(),
        name="stream-platform-detail",
    ),
    # You can add more paths here if needed
]

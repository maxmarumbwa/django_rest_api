from django.urls import path, include
from app.api.views import (
    WatchListAV,
    StreamPlatformAV,
    WatchDetailAV,
    StreamPlatformDetailAV,
    UserReview,
    WatchListGV,
)

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="watch-list"),
    path("list2/", WatchListGV.as_view(), name="watch-list"),
    path("<int:pk>/", WatchDetailAV.as_view(), name="watch-detail"),
    path("stream/", StreamPlatformAV.as_view(), name="stream-platform"),
    path(
        "stream/<int:pk>/",
        StreamPlatformDetailAV.as_view(),
        name="stream-platform-detail",
    ),
    path(
        "reviews/<str:username>/",
        UserReview.as_view(),
        name="user-review-detail",
    ),
    path(
        "reviews/",
        UserReview.as_view(),
        name="user-review-detail",
    ),
    # You can add more paths here if needed
]

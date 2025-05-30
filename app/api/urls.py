from django.urls import path, include
from app.api.views import MovieListAV, MovieDetailAV

urlpatterns = [
    path("list/", MovieListAV.as_view(), name="Movie-list"),
    path("<int:pk>/", MovieDetailAV.as_view(), name="Movie-Detail"),
    # You can add more paths here if needed
]

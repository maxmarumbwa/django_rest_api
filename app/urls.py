from django.urls import path, include
from app.views import movie_list, movie_detail

urlpatterns = [
    path("list/", movie_list, name="movie_list"),
    path("<int:movie_id>/", movie_detail, name="movie_detail"),
    # You can add more paths here if needed
]

# ####------CLASS BASED VIEWS------####
# import modules
from rest_framework.views import APIView
from app.models import WatchList, StreamPlatform
from app.api.serializers import WatchListSerializer, StreamPlatformSerializer

# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class StreamPlatformAV(APIView):
    def get(self, request):
        stream_platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(
            stream_platforms, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformDetailAV(APIView):
    def get(self, request, pk):
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(
                {"Error": "StreamPlatform not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = StreamPlatformSerializer(stream_platform)
        return Response(serializer.data)


class WatchListAV(APIView):
    def get(self, request):
        watchlist = WatchList.objects.all()
        serializer = WatchListSerializer(watchlist, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailAV(APIView):
    def get(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(
                {"Error": "WatchList not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = WatchListSerializer(watchlist)
        return Response(serializer.data)

    def put(self, request, pk):
        watchlist = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(watchlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        watchlist = WatchList.objects.get(pk=pk)
        watchlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ####------FUNCTION BASED VIEWS------####
# from app.models import Movie
# from app.api.serializers import MovieSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status


# @api_view(["GET", "POST"])
# def movie_list(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     if request.method == "POST":
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=400)


# @api_view(["GET", "PUT", "DELETE"])
# def movie_detail(request, movie_id):
#     if request.method == "GET":
#         try:
#             movie = Movie.objects.get(id=movie_id)
#         except Movie.DoesNotExist:
#             return Response(
#                 {"Error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND
#             )
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     if request.method == "PUT":
#         movie = Movie.objects.get(id=movie_id)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == "DELETE":
#         movie = Movie.objects.get(id=movie_id)
#         movie.delete()
#         # return Response(status=204)
#         return Response(status=status.HTTP_204_NO_CONTENT)

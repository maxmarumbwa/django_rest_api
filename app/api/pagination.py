from rest_framework.pagination import PageNumberPagination


class WatchListPagination(PageNumberPagination):
    page_size = 2

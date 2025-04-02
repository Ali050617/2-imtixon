from rest_framework.pagination import PageNumberPagination


class ProgressPagination(PageNumberPagination):
    page_size = 10

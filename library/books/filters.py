
import django_filters
from .models import books

class booksFilter(django_filters.FilterSet):
    class Meta:
        model = books
        fields = ("__all__")

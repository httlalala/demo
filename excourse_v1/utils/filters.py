import django_filters
from django_filters.rest_framework import FilterSet

from users.models import User


class UserViewFilter(FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains')
    phone = django_filters.CharFilter(lookup_expr='exact')
    class Meta:
        model = User
        fields  = ('username','phone')
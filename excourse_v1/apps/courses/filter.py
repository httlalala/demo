# #filters.py
# from django_filters import rest_framework as filters
#
# from courses.models import Course
#
#
# class BookFilter(filters.FilterSet):
#     min_read = filters.NumberFilter(field_name="bread", lookup_expr='gte')
#     max_read = filters.NumberFilter(field_name="bread", lookup_expr='lte')
#     class Meta:
#         model = Course  # 模型名
#         fields = ['grade','']
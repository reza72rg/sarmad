from django_filters import rest_framework as filters
from ...models import Student


class PostFilters(filters.FilterSet):
    age_min = filters.NumberFilter(field_name="age", lookup_expr="gte")
    age_max = filters.NumberFilter(field_name="age", lookup_expr="lte")

    class Meta:
        model = Student
        fields = {
            "username": ["exact", "in"],
            "age": ["exact"],


        }
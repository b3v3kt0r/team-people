import django_filters
from teams.models import Team


class TeamFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name="name",
        lookup_expr="icontains"
    )

    class Meta:
        model = Team
        fields = ["name"]

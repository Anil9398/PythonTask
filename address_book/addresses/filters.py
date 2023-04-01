from django_filters import rest_framework as filters
from addresses.models import Address

class AddressFilter(filters.FilterSet):
    distance = filters.NumberFilter(method="filter_distance")

    class Meta:
        model = Address
        fields = ["latitude", "longitude"]

    def filter_distance(self, queryset, name, value):
        lat = float(self.request.query_params.get("latitude"))
        lon = float(self.request.query_params.get("longitude"))
        distance = float(value)

        lat_range = distance / 111.0
        lon_range = distance / (111.0 * abs(lat))

        min_lat, max_lat = lat - lat_range, lat + lat_range
        min_lon, max_lon = lon - lon_range, lon + lon_range

        return queryset.filter(latitude__range=[min_lat, max_lat], longitude__range=[min_lon, max_lon])

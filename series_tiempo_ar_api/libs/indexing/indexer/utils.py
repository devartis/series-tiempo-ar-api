from django.db.models import Count
from django_datajsonar.models import Distribution, Field


def remove_duplicated_fields(distribution: Distribution):
    non_unique_ids = (distribution.field_set
                      .values_list('identifier', flat=True)
                      .annotate(identifier_count=Count('identifier'))
                      .filter(identifier_count__gt=1))

    for identifier in non_unique_ids:
        fields = Field.objects.filter(identifier=identifier).exclude(present=True)
        fields.delete()

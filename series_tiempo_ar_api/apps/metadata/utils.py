#! coding: utf-8
from typing import Sequence, List

from django.db.models import QuerySet
from elasticsearch_dsl import Search, Q
from django_datajsonar.models import Field
from series_tiempo_ar_api.apps.metadata import constants
from series_tiempo_ar_api.apps.metadata.models import CatalogAlias
from series_tiempo_ar_api.libs.indexing.elastic import ElasticInstance


def resolve_catalog_id_aliases(aliases: Sequence[str]) -> List[str]:
    """
    Expande cada término en la lista de aliases en los catalog_id que representa.
    Si algún alias no existe, se interpreta como un catalog_id directamente y
    se devuelve como está.
    """
    catalog_ids = []
    for catalog_id in aliases:
        try:
            catalog_ids.extend(CatalogAlias.objects.get(alias=catalog_id).resolve())
        except CatalogAlias.DoesNotExist:
            catalog_ids.append(catalog_id)

    return catalog_ids


def delete_metadata(fields: list):
    es_instance = ElasticInstance.get()

    search = Search(using=es_instance, index=constants.FIELDS_INDEX)
    return search.filter('terms', id=[field.identifier for field in fields]).delete()

#! coding: utf-8

METADATA_ALIAS = 'metadata'
METADATA_DOC_TYPE = 'doc'

PARAM_LIMIT = 'limit'
PARAM_OFFSET = 'start'
PARAM_QUERYSTRING = 'q'
PARAM_AGGREGATIONS = 'aggregations'

FILTER_ARGS = {
    # Pares nombre_arg: field del documento en elasticsearch
    'dataset_theme': 'dataset_theme',
    'units': 'units',
    'dataset_publisher_name': 'dataset_publisher_name',
    'dataset_source': 'dataset_source_keyword',
    'catalog_id': 'catalog_id',
}


ANALYZER = 'spanish_asciifold'
SYNONYM_FILTER = 'synonyms_filter'

DEFAULT_MIN_SCORE = 5

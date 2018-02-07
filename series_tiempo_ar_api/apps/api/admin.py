from django.contrib import admin

from .models import Catalog, Dataset, Distribution, Field


class DatasetAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'catalog', 'present', 'indexable')
    search_fields = ('identifier', 'catalog__identifier', 'present', 'indexable')
    readonly_fields = ('identifier', 'catalog')
    actions = ['make_indexable', 'make_unindexable']

    list_filter = ('catalog__identifier', 'present', 'indexable')

    def make_unindexable(self, _, queryset):
        queryset.update(indexable=False)
    make_unindexable.short_description = 'Marcar como no indexable'

    def make_indexable(self, _, queryset):
        queryset.update(indexable=True)
    make_indexable.short_description = 'Marcar como indexable'


class DistributionAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'dataset', 'get_catalog_id')
    search_fields = ('identifier', 'dataset__identifier', 'dataset__catalog__identifier')
    list_filter = ('dataset__identifier', 'dataset__catalog__identifier')

    def get_catalog_id(self, obj):
        return obj.dataset.catalog.identifier
    get_catalog_id.short_description = 'Catalog'
    get_catalog_id.admin_order_field = 'dataset__catalog__identifier'


class FieldAdmin(admin.ModelAdmin):
    list_display = ('series_id', 'distribution', 'get_dataset_id', 'get_catalog_id')
    search_fields = (
        'series_id',
        'distribution__identifier',
        'distribution__dataset__identifier',
        'distribution__dataset__catalog__identifier'
    )
    list_filter = (
        'distribution__identifier',
        'distribution__dataset__identifier',
        'distribution__dataset__catalog__identifier'
    )

    def get_catalog_id(self, obj):
        return obj.distribution.dataset.catalog.identifier
    get_catalog_id.short_description = 'Catalog'
    get_catalog_id.admin_order_field = 'distribution__dataset__catalog__identifier'

    def get_dataset_id(self, field):
        return field.distribution.dataset.identifier
    get_dataset_id.short_description = 'Dataset'
    get_dataset_id.admin_order_field = 'distribution__dataset__identifier'


admin.site.register(Catalog)
admin.site.register(Dataset, DatasetAdmin)
admin.site.register(Distribution, DistributionAdmin)
admin.site.register(Field, FieldAdmin)

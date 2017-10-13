#! coding: utf-8
from django.test import TestCase

from elastic_spike.apps.api.models import Catalog, Dataset, Distribution, Field
from elastic_spike.apps.api.pipeline import NameAndRepMode, Collapse
from elastic_spike.apps.api.query.query import Query


class NameAndRepModeTest(TestCase):
    """Testea el comando que se encarga del parámetro 'ids' de la 
    query: el parseo de IDs de series y modos de representación de las
    mismas.
    """
    single_series = 'random-0'
    single_series_rep_mode = 'random-0:percent_change'

    @classmethod
    def setUpClass(cls):
        catalog = Catalog.objects.create(title='test_catalog', metadata='{}')
        dataset = Dataset.objects.create(identifier="132",
                                         metadata={},
                                         catalog=catalog)

        distrib = Distribution.objects.create(identifier='132.1',
                                              metadata='{}',
                                              download_url="invalid_url",
                                              dataset=dataset)
        Field.objects.create(
            series_id=cls.single_series,
            metadata='{}',
            distribution=distrib,
            title='random-0'
        )
        super(cls, NameAndRepModeTest).setUpClass()

    def setUp(self):
        self.cmd = NameAndRepMode()
        self.query = Query()

    def test_invalid_series(self):
        invalid_series = 'invalid'
        self.cmd.run(self.query, {'ids': invalid_series})
        self.assertTrue(self.cmd.errors)

    def test_valid_series(self):
        self.cmd.run(self.query, {'ids': self.single_series})
        self.assertFalse(self.cmd.errors)


class CollapseTest(TestCase):
    single_series = 'random-0'

    def setUp(self):
        self.query = Query()
        self.cmd = Collapse()

    def test_valid_aggregation(self):
        self.cmd.run(self.query, {'ids': self.single_series,
                                  'collapse:': 'year',
                                  'collapse_aggregation': 'sum'})
        self.assertFalse(self.cmd.errors)

    def test_invalid_aggregation(self):
        self.cmd.run(self.query, {'ids': self.single_series,
                                  'collapse': 'year',
                                  'collapse_aggregation': 'INVALID'})
        self.assertTrue(self.cmd.errors)

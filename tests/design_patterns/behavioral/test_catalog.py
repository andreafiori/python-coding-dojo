from python_algorithms.design_patterns.behavioral.catalog import Catalog, CatalogInstance, CatalogClass, CatalogStatic

class TestCatalog:
    def test_catalog_main_method(self):
        test = Catalog('param_value_2')
        assert test.main_method() == 'executed method 2!'

    def test_catalog_instance_main_method(self):
        test = CatalogInstance('param_value_1')
        assert test.main_method() == 'Value x1'

    def test_catalog_class_main_method(self):
        test = CatalogClass('_class_method_2')
        assert test.main_method() == 'Value x2'

    def test_catalog_static_main_method(self):
        test = CatalogStatic('param_value_1')
        assert test.main_method() == 'executed method 1!'

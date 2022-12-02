import pytest
from conftest import Fields, TestFields
from supplier import models


class TestSupplierModel:
    def test_supplier_creation(self, supplier_test):
        assert supplier_test.user_name == TestFields['USER_NAME_TEST'].value
        assert supplier_test.first_name == TestFields['FIRST_NAME_TEST'].value
        assert supplier_test.last_name == TestFields['LAST_NAME_TEST'].value
        assert supplier_test.password == TestFields['PASSWORD_TEST'].value
        assert supplier_test.user_type == TestFields['USER_TYPE_TEST'].value
        assert supplier_test.business_name == TestFields['BUSINESS_NAME_TEST'].value

    @pytest.mark.django_db()
    def test_save_supplier(self, supplier_test):
        supplier_test.save()
        assert supplier_test in models.Supplier.objects.all()

    @pytest.mark.django_db()
    def test_delete_supplier(self, supplier_test):
        supplier_test.save()
        supplier_test.delete()
        assert supplier_test not in models.Supplier.objects.all()

    @pytest.mark.django_db()
    def test_filter_by_field(self, supplier_test):
        supplier_test.save()
        for attri, testAttri in zip(Fields, TestFields):
            print(models.Supplier.filter_by_field(attri.name,
                                                  testAttri.value))
        assert True

    @pytest.mark.django_db()
    def test_get_all_suppliers(self):
        for sup in models.Supplier.get_all_suppliers():
            assert sup in models.Supplier.objects.all()
        assert True

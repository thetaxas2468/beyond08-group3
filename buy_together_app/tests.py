import pytest
from buy_together_app.models import supplierProduct , Product, Supplier

supID0 = 123
supID1 = 222
supID2 = 127    
class TestSupProduct:

    @pytest.fixture
    def creat_product(self):
        prod0 = Product(qr_code = "AASSD22", product_name = "APPLE", description= "sweet!!")        
        prod1 = Product(qr_code = "QS#$HHS", product_name = "CARROT", description= "yummy!!")
        prod2 = Product(qr_code = "AAsdgv66", product_name = "BANANA", description= "great!!")
        prod0.save()
        prod1.save()
        prod2.save()
        return [prod0, prod1, prod2]

    @pytest.fixture
    def creat_supplier(self):
        sup0 = Supplier (user_name = "ali22", first_name = "ali" , last_name = "ab", password = "2345678", access = True)
        sup1 = Supplier(user_name = "max00", first_name = "Max" , last_name = "hani", password = "123456789", access = True)
        sup2 = Supplier (user_name = "rawanab", first_name = "rawan" , last_name = "abu", password = "0000000", access = True)
        sup0.save()
        sup1.save()
        sup2.save()     
        return [sup0, sup1, sup2]

    @pytest.fixture
    def creat_supProd(self, creat_product , creat_supplier):
        supprod0 = supplierProduct(suppler_product_id = supID0, user_name = creat_supplier[0], qr_code = creat_product[0], price = 22, quantity = 4) 
        supprod1 = supplierProduct(suppler_product_id = supID1, user_name = creat_supplier[1], qr_code = creat_product[1], price = 16, quantity = 3)
        supprod2 = supplierProduct(suppler_product_id = supID2, user_name = creat_supplier[2], qr_code = creat_product[2], price = 50, quantity = 8)
        supprod0.save()
        supprod1.save()
        supprod2.save()
        return [supprod0, supprod1, supprod2]
    
    @pytest.mark.django_db()
    def test_creation(self, creat_supProd):
        ss = creat_supProd[0]
        assert ss.suppler_product_id == supID0
        assert ss.quantity == 4
        assert ss.price == 22

    @pytest.mark.django_db
    def test_objectSavedInDb(self, creat_supProd):
        assert creat_supProd[2] in supplierProduct.objects.all()
    
    @pytest.mark.django_db
    def test_increase_productquantiy(self,creat_supProd):
        newquantity = 3
        assert creat_supProd[1].increase_productquantiy(self, newquantity)

    @pytest.mark.django_db
    def test_decrase_productquantity(self,creat_supProd):
        newq = 3
        assert creat_supProd[0].decrase_productquantity(creat_supProd[0],newq)
    @pytest.mark.django_db
    def test_deleting(self, creat_supProd):
        assert creat_supProd[0] in supplierProduct.objects.all()
        creat_supProd[0].delete()
        assert creat_supProd[0] not in supplierProduct.objects.all()

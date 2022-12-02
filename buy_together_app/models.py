from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=32, primary_key=True, null=False)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    password = models.CharField(max_length=16)
    access = models.BooleanField()

    class Meta:
        abstract = True


class Supplier(User):
    pass


class Product(models.Model):
    qr_code = models.CharField(max_length=32, primary_key=True)
    product_name = models.CharField(max_length=32)
    description = models.TextField()


class supplierProduct(models.Model):
    suppler_product_id = models.IntegerField(primary_key=True)
    qr_code = models.ForeignKey('Product', on_delete=models.CASCADE)
    user_name = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('suppler_product_id', 'qr_code')
    @staticmethod
    def increase_productquantiy(self, newquantity):
        self.quantity = newquantity
        return True

    @staticmethod
    def decrase_productquantity(supp, newquantity):
        if supp.quantity < newquantity :
            return False
        else: 
            x = supp.quantity
            supp.quantity = x - newquantity
            return True
    @staticmethod
    def adding_product(prod0, sup0, price0, quant0, suppid):
        return supplierProduct (suppler_product_id = suppid, user_name = sup0, qr_code = prod0, price = price0, quantity = quant0)
    
    
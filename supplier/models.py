from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=32,
                                 primary_key=True,
                                 null=False)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    password = models.CharField(max_length=16)
    user_type = models.CharField(max_length=16)

    class Meta:
        abstract = True


class Supplier(User):
    business_name = models.CharField(max_length=32)

    @staticmethod
    def filter_by_field(field, field_value):
        if hasattr(Supplier, str(field)):
            return Supplier.objects.filter(**{field: field_value})
        return None

    @staticmethod
    def get_all_suppliers():
        return Supplier.objects.all()

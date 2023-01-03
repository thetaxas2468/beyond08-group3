# Generated by Django 4.1.3 on 2023-01-03 09:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0002_test_data'),
        ('delivery_location', '0002_test_data'),
        ('supplier_product', '0002_test_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('delivery_location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 to='delivery_location.deliverylocation')),
                ('supplier_product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 to='supplier_product.supplierproduct')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
    ]

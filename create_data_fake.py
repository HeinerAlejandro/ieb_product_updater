import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ieb_product_updater.settings")
django.setup()

import decimal

from faker import Faker
from model_bakery.recipe import Recipe

from core.models import Product


fake = Faker()

for k in range(100):
    base_price = fake.pydecimal(
        left_digits=5, right_digits=2, positive=True, min_value=1000.00
    )

    product = Recipe(
        Product,
        description=fake.word(),
        buying_price=base_price,
        selling_price=base_price * decimal.Decimal(1.3),
    )

    product.make()

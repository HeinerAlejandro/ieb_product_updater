import string
import random

from django.db import models


# Create your models here.

def get_random_str():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))


class Product(models.Model):
    """Model Product"""

    code = models.TextField(
        verbose_name="Product ID",
        default=get_random_str,
        primary_key=True
    )

    buying_price = models.DecimalField(
        verbose_name="Buying Price",
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False
    )

    selling_price = models.DecimalField(
        verbose_name="Selling Price",
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False
    )

    description = models.TextField(
        verbose_name="Product Description",
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        verbose_name="Creation Datetime",
        auto_now_add=True
    )

    update_at = models.DateTimeField(
        verbose_name="Updating Datetime",
        auto_now=True
    )

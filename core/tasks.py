import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ieb_product_updater.settings")

import django

django.setup()

from django.db.models import F
from django.utils import timezone

from celery import shared_task

from .models import Product


@shared_task
def update_prices():
    Product.objects.all().update(
        selling_price=F("selling_price") * 1.1, update_at=timezone.now()
    )

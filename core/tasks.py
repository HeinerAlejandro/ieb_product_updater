import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ieb_product_updater.settings")

import django

django.setup()

from django.db.models import F
from celery.schedules import crontab

from ieb_product_updater.celery import app
from .models import Product


@app.task
def update_prices():
    Product.objects.all().update(F("selling_price") * 1.1)


@app.on_after_configure.connect()
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(
            minute=1,
        ),
        update_prices,
    )

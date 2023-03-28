import os

from celery import Celery
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ieb_product_updater.settings")
django.setup()

from django.conf import settings


app = Celery(
    "ieb_product_updater",
    broker_url=settings.BROKER_URL
)

app.config_from_object('ieb_product_updater:settings')

app.autodiscover_tasks()
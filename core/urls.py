from django.urls import path, include
from rest_framework import routers

from .views import ProductReadOnlyViewSet


router = routers.SimpleRouter()

router.register(r"products", ProductReadOnlyViewSet)

urlpatterns = [
    path("", include(router.urls))
]

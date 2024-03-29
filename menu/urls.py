# urls.py
from django.urls import path, include
from .views import MenuItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"menu", MenuItemViewSet)
app_name = "menu"
urlpatterns = [
    path("", include(router.urls)),
]

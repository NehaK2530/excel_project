from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from file_app.views import ProductViewSet


router = DefaultRouter()
router.register('products',ProductViewSet, basename='products')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),


]

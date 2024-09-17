
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api.views import ProductViewSet


router = routers.DefaultRouter()
router.register('product', ProductViewSet, 'product')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

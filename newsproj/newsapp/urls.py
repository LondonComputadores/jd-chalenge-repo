from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'api/category', CategoryViewSet)
router.register(r'api/authors', AuthorsViewSet)
router.register(r'api/articles', ArticlesViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
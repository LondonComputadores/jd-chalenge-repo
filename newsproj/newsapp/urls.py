from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'api/v2/category/', CategoryViewSet)
router.register(r'api/v2/authors/', AuthorsViewSet)
router.register(r'api/v2/articles', ArticlesViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
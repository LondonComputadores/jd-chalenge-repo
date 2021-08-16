"""newsproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from rest_framework import routers
from newsapp.views import ArticlesViewSet
from newsapp import views
from newsapp.urls import router

# # Swagger documentation setup
# schema_view = get_schema_view(
#     openapi.Info(
#         title="Articles_API",
#         default_version='v1',
#         description="Test description",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@snippets.local"),
#         license=openapi.License(name="MIT License"),
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny],
# )



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/admin/', include(router.urls)),
    path('api/', include('accounts.urls')),
    path('api/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('api/v2/', include('rest_framework.urls')),
    path('api/v2/category/', include(router.urls)),
    path('api/v2/authors/', include(router.urls)),
    path('api/v2/articles/', include(router.urls)),
]

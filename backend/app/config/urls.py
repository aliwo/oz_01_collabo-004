"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/v1/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/v1/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),
    path("api/v1/user/", include("users.urls")),
    path("api/v1/category/", include("categories.urls")),
    # path('accounts/', include('accounts.urls')), # 소셜 로그인 계정 관련 urls
    # path('accounts/', include('allauth.urls')), # 소셜로그인 관련 urls
    path("api/v1/product/", include("products.urls")),
    path("api/v1/wishlist/", include("wishlist.urls")),
    # path('api/v1/order/', include('orders.urls')),
    path('api/v1/review/', include('reviews.urls')),
    # path('api/v1/post/', include('posts.urls')),
]

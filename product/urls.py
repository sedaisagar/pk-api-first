from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from product.views import (
    ProductViewSet,
    AdminProductCreateView,
    VendorProductUpdateView,
    CustomerProductListView,
)


router.register("products", ProductViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("admin/create/", AdminProductCreateView.as_view()),
    path("vendor/update/<int:pk>/", VendorProductUpdateView.as_view()),
    path("customer/list/", CustomerProductListView.as_view()),
]

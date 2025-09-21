from rest_framework import viewsets , generics

from product.serializers import ProductSerializer
from product.models import Product

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from utils.custom_perm import IsAdmin, IsCustomer, IsVendor

from drf_spectacular.utils import extend_schema

@extend_schema(tags=["Product"])
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



# Only Admin Access
@extend_schema(tags=["Admin Api(s)"])
class AdminProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdmin]

# Only Vendor Can Update
@extend_schema(tags=["Vendor Api(s)"])
class VendorProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsVendor]

# Only Customer Can View
@extend_schema(tags=["Customer Api(s)"])
class CustomerProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsCustomer]



from django.views import generic

class HomePageView(generic.TemplateView):
    template_name = "index.html"
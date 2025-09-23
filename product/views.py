import base64
import json
from django.shortcuts import redirect
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

class PaymentSuccesView(generic.TemplateView):
    template_name = "success.html"    

    def get(self, request, *args, **kwargs):
        params = request.GET.dict()

        """In Case Of Khalti We Can Try And Read status in query params"""
        if "status" in params:
            if params["status"] == "Completed":
                # Payment was successful
                print("Payment completed successfully.")
                return redirect("payment-success")

            return redirect("payment-failure")

        
        """In Case Of eSewa We Can Try And Read data in query params"""
        if "data" in params:
            data = params["data"]
            # Further processing can be done here
            try:
                decoded_data = json.loads(base64.b64decode(data).decode('utf-8'))
                if decoded_data.get("status") == "COMPLETE":
                    print("eSewa Payment completed successfully.")
                    return redirect("payment-success")
            except Exception as e:
                print("Error: Invalid token." ,e )

            return redirect("payment-failure")

        return super().get(request, *args, **kwargs)

class PaymentFailureView(generic.TemplateView):   
    template_name = "failure.html"
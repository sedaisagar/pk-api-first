from rest_framework import  views
from rest_framework.response import Response
from apis.icon.serializers import IconSerializer

from drf_spectacular.utils import extend_schema

@extend_schema(tags=["Icon Maker"])
class IconMakerFromImageView(views.APIView):
    serializer_class = IconSerializer

    def post(self, request, *args, **kwargs):
        # Django => request.POST
        # Rest Framework => request.data
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)
    

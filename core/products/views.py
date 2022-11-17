from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductsAPIView(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        product = super().create(request, *args, **kwargs)
        return Response(
            status=status.HTTP_201_CREATED,
            data=ProductSerializer(product.data.serializer.instance).data,
        )

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.status_code = status.HTTP_201_CREATED
        return response

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class PostProductAPIView(ProductsAPIView):
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        product = super().create(request, *args, **kwargs)
        data = ProductSerializer(product.data.serializer.instance).data
        return Response(
            status=status.HTTP_201_CREATED,
            data=data,
        )

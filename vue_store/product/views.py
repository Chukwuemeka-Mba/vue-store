from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

class LatestProductsList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def list(self, request):
        data = self.get_queryset()[:4]
        serializer = ProductSerializer(data=data, many=True, context={"request":request})
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
class ProductDetail(generics.RetrieveAPIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.get(category__slug=category_slug, slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object( category_slug, product_slug)
        serializer = ProductSerializer(product, context={'request':request})
        return Response(serializer.data)




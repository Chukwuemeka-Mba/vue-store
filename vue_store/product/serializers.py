from rest_framework import serializers
from django.urls import reverse

from .models import Category, Product
from django.contrib.sites.shortcuts import get_current_site
class ProductSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "category",
            "slug",
            "absolute_url",
            "description",
            "price",
            "image_url",
            "thumbnail_url",
        )
        depth = 2
        
    def get_absolute_url(self, obj):
        request = self.context.get("request")
        domain = get_current_site(request).domain
        url = f"http://{domain}{reverse('product:product-detail', args=[obj.category.slug, obj.slug])}"
        return url
      
    def get_image_url(self, obj):
        request = self.context.get("request")
        domain = get_current_site(request).domain
        url = f"http://{domain}{obj.get_image()}"
        return url
    
    def get_thumbnail_url(self, obj):
        request = self.context.get("request")
        domain = get_current_site(request).domain
        url = f"http://{domain}{obj.get_thumbnail()}"
        return url

        # url = f"http://{domain}/api/v1/products{obj.get_absolute_url()}"

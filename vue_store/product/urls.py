from django.urls import path, include
from product import views

app_name = "product"

urlpatterns = [
    path('/latest-products/', views.LatestProductsList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
]
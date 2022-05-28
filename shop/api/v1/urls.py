from django.urls import path
from api.v1.product.views import ProductView
from api.v1.category.views import CategoryView

urlpatterns = [
    path("product/", ProductView.as_view(), name="api_product_list"),
    path("product/<int:pk>/", ProductView.as_view(), name="api_product_one"),




    path("category/", CategoryView.as_view(), name="api_category_list"),
    path("category/<int:pk>/", CategoryView.as_view(), name="api_category_one"),
]
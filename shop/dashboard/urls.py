from django.urls import path
from .views import *
from .product import views as product_view
from .category import views as category_view

urlpatterns = [
    path('', index, name="dashboard"),
    path('product/list/', product_view.list, name="dashboard_product_list"),
    path('product/detail/<int:pk>', product_view.list, name="dashboard_product_detail"),
    path('product/add/', product_view.product_add, name="dashboard_product_add"),
    path('product/edit/<int:pk>', product_view.product_add, name="dashboard_product_edit"),
    path('product/delete/<int:pk>', product_view.product_delete, name="dashboard_product_delete"),




    path('category/list', category_view.list, name="dashboard_category_list"),
    path('category/detail/<int:pk>', category_view.list, name="dashboard_category_detail"),
    path('category/add/', category_view.category_add, name="dashboard_category_add"),
    path('category/edit<int:pk>/', category_view.category_edit, name="dashboard_category_edit"),
    path('category/delete<int:pk>/', category_view.category_delete, name="dashboard_category_delete"),
]
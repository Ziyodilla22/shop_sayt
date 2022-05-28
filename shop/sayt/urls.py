from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("blog/", blog, name="blog"),
    path("blog_post/", blog_post, name="blog_post"),
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
    path("contact/", contact, name="contact"),
    path("shop/", shop, name="shop"),
    path("shop_single/", shop_single, name="shop_single"),
]
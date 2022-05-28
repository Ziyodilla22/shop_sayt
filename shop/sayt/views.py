from django.shortcuts import render
from .models import *


def index(requests):
    product = Product.objects.all()
    print(product)
    ctx = {
        "product": product
    }
    return render(requests, "index.html", ctx)


def about(requests):
    ctx = {}
    return render(requests, "about.html", ctx)


def blog(requests):
    ctx = {}
    return render(requests, "blog.html", ctx)


def blog_post(requests):
    ctx = {}
    return render(requests, "blog-post.html", ctx)


def cart(requests):
    ctx = {}
    return render(requests, "cart.html", ctx)


def checkout(requests):
    ctx = {}
    return render(requests, "checkout.html", ctx)


def contact(requests):
    ctx = {}
    return render(requests, "contact-us.html", ctx)


def shop(requests):
    ctx = {}
    return render(requests, "shop.html", ctx)


def shop_single(requests):
    ctx = {}
    return render(requests, "shop-single.html", ctx)

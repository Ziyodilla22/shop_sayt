from django.shortcuts import render, redirect

from dashboard.product.forms import ProductForm
from sayt.models import Product


def list(requests, pk=None):
    if pk:
        products = Product.objects.get(pk=pk)

        html = "dashboard/product/detail.html"
        ctx = {
            "product": products

        }
    else:
        products = Product.objects.all()
        html = "dashboard/product/list.html"
        ctx = {
            "products": products
        }

    return render(requests, html, ctx)


def product_add(requests, pk=None):
    html = "dashboard/product/forms.html"
    form = ProductForm
    if pk:
        root = Product.objects.get(pk=pk)
    else:
        root = None

    form = ProductForm(instance=root)

    if requests.POST:
        forms = ProductForm(requests.POST, requests.FILES, instance=root)

        if forms.is_valid():
            forms.save()
            return redirect("dashboard_product_list")
        else:
            print(forms.errors)

    ctx = {
        "form": form

    }

    return render(requests, html, ctx)


def product_delete(requests, pk):
    root = Product.objects.get(pk=pk)
    root.delete()

    return redirect("dashboard_product_list")


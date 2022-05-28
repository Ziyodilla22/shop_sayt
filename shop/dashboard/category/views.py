from django.shortcuts import render, redirect

from dashboard.category.forms import CategoryForm

from sayt.models import Category


def list(requests, pk=None):
    if pk:
        category = Category.objects.get(pk=pk)

        html = "dashboard/category/detail.html"
        ctx = {
            "category": category

        }
    else:
        category = Category.objects.all()
        html = "dashboard/category/list.html"
        ctx = {
            "category": category
    }

    return render(requests, html, ctx)


def category_add(requests):
    html = "dashboard/category/forms.html"
    form = CategoryForm

    if requests.POST:
        forms = CategoryForm(requests.POST, requests.FILES)

        if forms.is_valid():
            forms.save()
            return redirect("dashboard_category_list")
        else:
            print(forms.errors)

    ctx = {
        "form": form

    }

    return render(requests, html, ctx)

def category_edit(requests, pk):
    html = "dashboard/category/forms.html"
    root = Category.objects.get(pk=pk)

    form = CategoryForm(instance=root)

    if requests.POST:
        forms = CategoryForm(requests.POST, requests.FILES, instance=root)

        if forms.is_valid():
            forms.save()
            return redirect("dashboard_category_list")
        else:
            print(forms.errors)

    ctx = {
        "form": form

    }

    return render(requests, html, ctx)


def category_delete(requests, pk):
    root = Category.objects.get(pk=pk)
    root.delete()

    return redirect("dashboard_category_list")
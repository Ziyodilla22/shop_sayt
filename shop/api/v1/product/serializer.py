from rest_framework import serializers

from sayt.models import Product


class ProductForm(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"



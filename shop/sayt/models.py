from django.db import models

# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)

        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    color = models.CharField(max_length=256)
    price = models.TextField(max_length=256)
    new_price = models.TextField(max_length=256)
    img = models.ImageField()
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

from rest_framework import response
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import NotFound

from sayt.models import Category
from .serializer import CategoryForm
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .services import get_list, get_one


class CategoryView(GenericAPIView):
    serializer_class = CategoryForm
    permission_classes = (AllowAny,)

    def get_object(self, pk=None):
        try:
            root = Category.objects.get(pk=pk)
        except:
            raise NotFound("object topilmadi")
        return root

    def get(self, requests, *args, **kwargs):
        if "pk" in kwargs and kwargs['pk']:
            resource = get_one(requests, kwargs['pk'])
        else:
            resource = get_list(requests)
            print(resource)


        return Response(resource, status=HTTP_200_OK, content_type="application/json")


    def post(self, requests, *args, **kwargs):
        pass

    def put(self, requests, pk, *args, **kwargs):
        pass

    def delete(self, requests, *args, **kwargs):
        pass

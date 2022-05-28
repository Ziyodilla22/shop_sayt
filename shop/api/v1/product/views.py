from rest_framework import response
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import NotFound
from sayt.models import Product
from .serializer import ProductForm
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .services import get_list, get_one


class ProductView(GenericAPIView):
    serializer_class = ProductForm
    permission_classes = (AllowAny, )

    def get_object(self, pk=None):
        try:
            root = Product.objects.get(pk=pk)
        except:
            raise NotFound("object topilmadi")
        return root

    def get(self, requests, *args, **kwargs):
        if "pk" in kwargs and kwargs['pk']:
            resource = get_one(requests, kwargs['pk'])
        else:
            resource = get_list(requests)


        return Response(response, status=HTTP_200_OK, content_type="application/json")





    def post(self, requests, *args, **kwargs):
        data = requests.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(reise_exeption=True)
        root = serializer.create(serializer.data)
        response = get_one(requests, root.id)

        return Response(response, status=HTTP_200_OK, content_type="application/json")



    def put(self, requests, pk, *args, **kwargs):
        data = requests.data
        root = self.get_object(kwargs['pk'])
        serializer = self.get_serializer(data=data, instance=root, partial=True)
        serializer.is_valid(reise_exeption=True)
        root = serializer.save()
        response = get_one(requests, root.id)

        return Response(response, status=HTTP_200_OK, content_type="application/json")

    def delete(self, requests, *args, **kwargs):
        root = self.get_object(kwargs['pk'])
        root.delete()
        response = {"result:": f"{root} object deleted"}
        return Response(response, status=HTTP_200_OK, content_type="application/json")



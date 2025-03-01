from django.shortcuts import render
from rest_framework import generics
from django.forms.models import model_to_dict

from .apps import CarsConfig
from .models import Car
from .serializers import CarSerializer
from rest_framework.response import Response

# class CarsAPIView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer

class CarsAPIView(generics.ListAPIView):
    def get(self, request):
        c = Car.object.all()
        return Response({'posts': CarSerializer(c, many = True).data})

    def post(self, request):
        serializer = CarSerializer(data = request.data)
        serializer.is_valid(raise_execption = True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Car.objects.get(pk = pk)
        except:
            return  Response({"error": "Method PUT not allowed"})

        serializer = CarSerializer(data = request.data, instance = instance)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        #управление записями с переданным pk

        return Response({"post": "delete post" + str(pk)})

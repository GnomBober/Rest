from django.shortcuts import render
from rest_framework import generics
from django.forms.models import model_to_dict
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

        post_new = Car.objects.create(
            title = request.data['title'],
            content = request.data['content'],
            cat_id = request.data['cat_id']
        )

        return Response({'post': model_to_dict(post_new).data})

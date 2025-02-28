from django.shortcuts import render
from rest_framework import generics
from .models import Car
from .serializers import CarSerializer
from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response

class CarsAPIView(APIView):
    def get(self, request):
        lst = Car.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = Car.objects.create(
            title = request.data['title'],
            content = request.data['content'],
            cat_id = request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})

# class CarsAPIView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer

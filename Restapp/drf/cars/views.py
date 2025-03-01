from django.shortcuts import render
from rest_framework import generics, viewsets
from django.forms.models import model_to_dict
from rest_framework.decorators import action
from .apps import CarsConfig
from .models import Car, Category
from .permissions import *
from .serializers import CarSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

class CarsAPIList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class CarsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class CarsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminOrReadOnly,)

# class CarsViewSet(viewsets.ModelViewSet):
#     # queryset = Car.objects.all()
#     serializer_class = CarSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#
#         if not pk:
#             return Car.odjects.all()[:3]
#
#         return Car.objects.filter(pk = pk)
#
#     @action(methods = ['get'], detail = False)
#     def category(self, request, pk = None):
#         cats = Category.objects.get(pk = pk)
#         return Response({'cats': cats.name})

# class CarsAPIView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer

# class CarsAPIList(generics.ListCreateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#
# class CarsAPIUpdate(generics.UpdateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#
# class CarsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer

# class CarsAPIView(APIView):
#     def get(self, request):
#         c = Car.objects.all()
#         return Response({'posts': CarSerializer(c, many = True).data})
#
#     def post(self, request):
#         serializer = CarSerializer(data = request.data)
#         serializer.is_valid(raise_execption = True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Car.objects.get(pk = pk)
#         except:
#             return  Response({"error": "Method PUT not allowed"})
#
#         serializer = CarSerializer(data = request.data, instance = instance)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         #управление записями с переданным pk
#
#         return Response({"post": "delete post" + str(pk)})

import io

from rest_framework import serializers
from .models import Car
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# class CarsModel:
#     def __init__(self, title, content):
#         self.title = title,
#         self.content = content

class CarSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only = True)
    time_update = serializers.DateTimeField(read_only = True)
    is_published = serializers.BooleanField(default=True)
    cat = serializers.IntegerField()

# class CarSerializer(serializers.ModelSerializer):
#     title = serializers.CharField(max_length = 255)
#     contenet = serializers.CharField()

# def encode():
#     model = CarsModel('bobslav', 'content: mashina')
#     model_sr = CarSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep = '\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title": "sobakoslava", "content": "content: zachem"')
#     data = JSONParser().parse(stream)
#     serializer = CarSerializer(data = data)
#     serializer.is_valid()
#     print(serializer.validated_data)

# class CarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Car
#         fields = ('title', 'cat_id')
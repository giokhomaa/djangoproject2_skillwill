from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import Car
from . serializers import CarSerializer


class SelectCarsView(APIView):
    def get(self, request):
        data = Car.objects.all()
        serializer = CarSerializer(data, context={'request':request}, many=True)
        return Response(serializer.data)

class AddCarView(APIView):
    def post(self, request):
        serializer = CarSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DeleteCarView(APIView):
    def delete(self, request, pk):
        event = Car.objects.get(pk=pk)
        event.delete()
        return Response("Deletion successful")



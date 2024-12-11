from django.shortcuts import render

from myAdmin.models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class ProductCreateAPIView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Product saved successfully"}, status=201)
        return Response(serializer.errors, status=400)
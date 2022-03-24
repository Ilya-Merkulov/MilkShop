from django.shortcuts import render
from rest_framework.views import APIView
from MilkShop.apps.product.models import Product, ProductReview
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from .serializers import ProductSerializer, ProductReviewSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class ProductList(APIView):
    """
          List all products, or create a new user.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    pass


class ProductReviewList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        product_review = ProductReview.objects.all()
        serializer = ProductReviewSerializer(product_review, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ProductReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
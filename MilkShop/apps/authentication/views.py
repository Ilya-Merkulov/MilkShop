from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from .serializers import UserSerializer, RegisterUserSerializer
from .models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.
# @api_view(['GET'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def UsersView(request):
#     if request.method == 'GET':
#         users = User.objects.all()
#         users_serializer = UserSerializer(users, many=True)
#         return JsonResponse(users_serializer.data, safe=False)

# class UserRegistration(generics.ListCreateAPIView):
#     @permission_classes([AllowAny])
#     def create(self, request, *args, **kwargs):
#         serializer = RegisterUserSerializer(data=request.data)
#         if serializer.is_valid():
#             self.perform_create(serializer)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#

class UserList(APIView):
    """
        List all users, or create a new user.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
        Retrieve, update or delete a user instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, requesl, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=requesl.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





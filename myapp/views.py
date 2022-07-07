from django.shortcuts import render
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer 
from rest_framework import status
from rest_framework  import viewsets
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.authentication import SessionAuthentication
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from .custompermissions import MyPermission

class usr(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes = [MyPermission]

































#     def list(self,request):
#         usr = User.objects.all()
#         ser = UserSerializer(usr, many=True)
#         return Response(ser.data)
    
#     def retrieve(self,request,pk=None):
#         id = pk
#         if id is not None:
#             usr = User.objects.get(id=id)
#             ser = UserSerializer(usr)
#             return Response(ser.data)
#     def create(self,request):
#         ser = UserSerializer(data=request.data)
#         if ser .is_valid():
#             ser.save()
#             return Response({'msg':"data is created successfully"},status=status.HTTP_201_CREATED)
#         return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def update(self,request,pk):
#         id = pk
#         usr = User.objects.get(id=id)
#         ser = UserSerializer(usr,data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response({'msg':"data is updated successfully"})
#         return Response(ser.errors)
#     def partial_update(self,request,pk):
#         id = pk
#         usr = User.objects.get(id=id)
#         ser = UserSerializer(usr,data=request.data, partial=True)
#         if ser.is_valid():
#             ser.save()
#             return Response({'msg':"data is partial updated successfully"})
#         return Response(ser.errors)
#     def destroy(self,request,pk):
#         id = pk
#         usr = User.objects.get(id=id)
#         usr.delete()
#         return Response({'msg':"data is deleted"})
     
    
            
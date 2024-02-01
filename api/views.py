from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
# Create your views here.

class TodoAPIView(APIView):
    serializer_class   = TodoSerializer
    permisson_classes  = [AllowAny]
    

    def get(self, request, format=None):
        todo        = Todo.objects.all()
        serializer  = TodoSerializer(todo, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = TodoSerializer(data=request.data)    
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class EditAPIView(APIView):
    serializer_class   = EditSerializer
    permission_classes = [AllowAny]

    def put(self, request, pk):
        try:
            data - EditSerializer(data=request.data)
            data.is_valid(raise_exception=False)
            valid_data = data.data

            getTodo = Todo.objects.get(pk=pk)
            if valid_data["done"]==True:
                getTodo.done = True
            else:
                getTodo.done = False

            if valid_data["name"]:
                getTodo.name = valid_data["name"]
            if valid_data["description"]:
                getTodo.descripton = valiid_data["description"]
            getTodo.save()   

        except Todo.DoesNotExist:
            return Response({
                "message":"Todo not found"
                },status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
				"message":str(e)
				}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteAPIView(APIView):
    permission_classes = [AllowAny]    

    def delete(self, request, pk):
        try:
            getTodo = Todo.objects.get(pk=pk)
            getTodo.delete()
            return Response({
                "message":"Todo Deleted Successfully"
            }, status=status.HTTP_200_OK)

        except Todo.DoesNotExist:
            return Response({
                "message":"Todo not found"
                },status=status.HTTP_404_NOT_FOUND)                                      

        except Exception as e:
            return Response({
				"message":str(e)
				}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from.models import Retrieve
from .serializer import Step1Serializer,AboutTheChildSerializer , Step3Serializer, LocationSerializer, RetrieveSerializer
# from .models import Retrieve
@api_view(['post'])
def Step1(request):
   try:
     new_user = Step1Serializer (data=request.data)

     if new_user.is_valid():
      new_user.save()

      return Response(new_user.data, status=status.HTTP_201_CREATED)
     else:
      return Response(new_user.errors, status=status.HTTP_400_BAD_REQUEST)
   
   except BaseException as e: 
      return Response(str(e))

@api_view(['post'])
def Step2(request):
   try:
     new_user = AboutTheChildSerializer (data=request.data)

     if new_user.is_valid():
      new_user.save()

      return Response(new_user.data, status=status.HTTP_201_CREATED)
     else:
      return Response(new_user.errors, status=status.HTTP_400_BAD_REQUEST)
   
   except BaseException as e: 
      return Response(str(e))

@api_view(['post'])
def Location(request):
   try:
     new_user = LocationSerializer(data=request.data)

     if new_user.is_valid():
      new_user.save()

      return Response(new_user.data, status=status.HTTP_201_CREATED)
     else:
      return Response(new_user.errors, status=status.HTTP_400_BAD_REQUEST)
   
   except BaseException as e: 
      return Response(str(e))
      
@api_view(['post'])
def Step3(request):
   try:
     new_user = Step3Serializer (data=request.data)

     if new_user.is_valid():
      new_user.save()

      return Response(new_user.data, status=status.HTTP_201_CREATED)
     else:
      return Response(new_user.errors, status=status.HTTP_400_BAD_REQUEST)
   
   except BaseException as e: 
      return Response(str(e))
  
@api_view(['GET'])
def retrieve_data(request, id):
    try:
        retrieve_instance = Retrieve.objects.filter(id=id)  
        serializer = RetrieveSerializer(retrieve_instance) 
        return Response(serializer.data, status=200)
    except Retrieve.DoesNotExist:
        return Response({"error": "Retrieve instance not found"}, status=404)
  
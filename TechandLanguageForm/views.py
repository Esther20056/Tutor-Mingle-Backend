from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import TechSkillsTwoSerializer, TechSkillsThreeSerializer, LocationSerializer, TechSkillsSerializer, LanguageFirstSerializer 
from .serializer import LanguageLessonSerializer, LanguageFormsubmissionSerializer

@api_view(['post'])
def TechSkills(request):
   try:
     new_user = TechSkillsSerializer(data=request.data)

     if new_user.is_valid():
      new_user.save()

      return Response(new_user.data, status=status.HTTP_201_CREATED)
     else:
      return Response(new_user.errors, status=status.HTTP_400_BAD_REQUEST)
   
   except BaseException as e: 
      return Response(str(e))

@api_view(['post'])
def TechSkillsTwo(request):
   try:
     new_user = TechSkillsTwoSerializer(data=request.data)

     if new_user.is_valid():
      new_user.save()

      return Response(new_user.data, status=status.HTTP_201_CREATED)
     else:
      return Response(new_user.errors, status=status.HTTP_400_BAD_REQUEST)
   
   except BaseException as e: 
      return Response(str(e))
    
@api_view(['post'])
def TechSkillThree(request):
   try:
     new_user = TechSkillsThreeSerializer(data=request.data)

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
def LanguageFirst(request):
   try:
     new_user = LanguageFirstSerializer(data=request.data)

     if new_user.is_valid():
      new_user.save()

      return Response(new_user.data, status=status.HTTP_201_CREATED)
     else:
      return Response(new_user.errors, status=status.HTTP_400_BAD_REQUEST)
   
   except BaseException as e: 
      return Response(str(e))

@api_view(['post'])
def LanguageLessonRequest(request):
   try:
     new_user = LanguageLessonSerializer(data=request.data)

     if new_user.is_valid():
      new_user.save()

      return Response(new_user.data, status=status.HTTP_201_CREATED)
     else:
      return Response(new_user.errors, status=status.HTTP_400_BAD_REQUEST)
   
   except BaseException as e: 
      return Response(str(e))

@api_view(['post'])
def LanguageFormRequest(request):
   try:
     new_user = LanguageFormsubmissionSerializer(data=request.data)

     if new_user.is_valid():
      new_user.save()

      return Response(new_user.data, status=status.HTTP_201_CREATED)
     else:
      return Response(new_user.errors, status=status.HTTP_400_BAD_REQUEST)
   
   except BaseException as e: 
      return Response(str(e))

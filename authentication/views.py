import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from authentication.models import User
from .serializers import (
    AboutUserSerializer,
    SignUpTwoSerializer,
    UserDetailSerializer,
    UserSerializer,
    SignUpThreeSerializer, TutoringExperienceSerializer,
    loginSerializer, CapturedImageSerializer
)
from django.core.mail import send_mail
from django.conf import settings
import logging
from .models import EmailVerificationToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def UserData(request):
    try:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_notification_email() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
logger = logging.getLogger(__name__)
def send_notification_email():
    try:
        send_mail(
            'New User Signup',
            'A new user has signed up on your website.',
            settings.DEFAULT_FROM_EMAIL,
            ['estherolajide456@gmail.com'],
            fail_silently=False,
        )
        print('Notification email sent successfully.') 
    except Exception as e:
        print(f'Error sending email: {e}') 

@api_view(['POST'])
def About(request):
    try:
        data = request.data.copy()
        data['user'] = request.user.id 

        serializer = AboutUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def getUser(request, id):
    logger.info(f"Received request to get user with id {id}")
    try:
        user = User.objects.get(id=id)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        logger.error(f"User with id {id} not found.")
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {str(e)}")
        return Response({'error': 'An unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def SignUpTwoData(request):
    try:
        serializer = SignUpTwoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def SignUpThreeData(request):
    try:
        serializer = SignUpThreeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def TutorExperience(request):
    try:
        serializer = TutoringExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def Login(request):
    serializer = loginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        user_data = {
            "phone": user.phone,
            "email": user.email,
            "id": user.id,
        }
        return Response(user_data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def capture_image(request):
    try:
        serializer = CapturedImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def send_confirmation_email(request):
    try:
        data = json.loads(request.body)
        user_id = data.get('user_id')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'message': 'User does not exist'}, status=404)
        logger.info(f'Email sent to user {user_id}')
        return Response({'message': 'Email sent successfully'})
    except Exception as e:
        logger.error(f'Failed to send email: {e}')
        return Response({'message': 'Failed to send email', 'error': str(e)}, status=500)
logger = logging.getLogger(__name__)

@api_view(['GET'])
def confirm_email(request, token):
    try:
        token_obj = EmailVerificationToken.objects.get(token=token)
        if token_obj.is_valid():
            user = token_obj.user
            user.is_active = True
            user.save()
            token_obj.delete()
            logger.info(f'Email verified and user activated: {user.email}')
            return Response({'message': 'Email confirmed successfully.'}, status=status.HTTP_200_OK)
        else:
            logger.warning(f'Invalid or expired token: {token}')
            return Response({'message': 'The token has expired or is invalid.'}, status=status.HTTP_400_BAD_REQUEST)
    
    except EmailVerificationToken.DoesNotExist:
        logger.error(f'Token not found: {token}')
        return Response({'message': 'The token does not exist.'}, status=status.HTTP_404_NOT_FOUND)


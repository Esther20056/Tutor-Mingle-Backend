from django.urls import path
from authentication.views import About, Login, SignUpThreeData, SignUpTwoData, UserData, capture_image, confirm_email, getUser, send_confirmation_email,  TutorExperience

urlpatterns = [
  path('first/', UserData),
  path('aboutuser/', About), 
  path('signuptwo/', SignUpTwoData), 
  path('getuser/<int:id>/', getUser),
  path('send-confirmation-email/',send_confirmation_email),
  path('confirm-email/<str:token>/', confirm_email),
  path('signupthree/', SignUpThreeData), 
  path('login/', Login),
  path('capturedimage/', capture_image),
  path('tutor_experience/', TutorExperience)
]
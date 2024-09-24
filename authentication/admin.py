from django.contrib import admin
from .models import  AboutUser, SignUpTwo,User, CapturedImage, EmailVerificationToken,SignUpThree, TutoringExperience


admin.site.register(AboutUser)
admin.site.register(User)
admin.site.register(SignUpTwo)
admin.site.register(SignUpThree)
admin.site.register(CapturedImage)
admin.site.register(EmailVerificationToken)
admin.site.register(TutoringExperience)
from django.urls import path
from .views import TechSkillsTwo, TechSkillThree, Location, TechSkills,LanguageFirst, LanguageLessonRequest
from .views import LanguageFormRequest
urlpatterns = [
    path('techskills/',TechSkills),
    path('techskilltwo/',TechSkillsTwo),
    path('techskillthree/',TechSkillThree),
    path('location/',Location),
    path('languagefirst/',LanguageFirst),
    path('languagelesson/',LanguageLessonRequest),
    path('languageform/',LanguageFormRequest),
]
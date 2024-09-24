from django.contrib import admin
from .models import LanguageFirstRequest, LanguageLesson, LanguageFormSubmission, TechSkills, TechskillsThree, TechSkillsTwo, Location

admin.site.register(LanguageFirstRequest),
admin.site.register(LanguageLesson),
admin.site.register(LanguageFormSubmission),
admin.site.register(TechSkills),
admin.site.register(TechSkillsTwo),
admin.site.register(TechskillsThree),
admin.site.register(Location),
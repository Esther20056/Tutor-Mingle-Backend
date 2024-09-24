from rest_framework import serializers
from .models import TechSkillsTwo, TechskillsThree,Location,TechSkills, LanguageFirstRequest,LanguageLesson, LanguageFormSubmission
from authentication.models import User

class TechSkillsTwoSerializer(serializers.ModelSerializer):
    class Meta:
         model= TechSkillsTwo
         fields='__all__'         
    def create(self, data):
        user = TechSkillsTwo.objects.create(
          child_name = data['child_name'],
          gender = data['gender'],
          age = data['age'],
          course = data['course'],
          goal = data['goal'],
          tutor_gender = data['tutor_gender'],
          about_the_child = data['about_the_child'],
        )
        return user

class  TechSkillsThreeSerializer(serializers.ModelSerializer):
  class Meta:
    model = TechskillsThree
    fields = '__all__'    
    def create(self, data):
        print(data['days_available'])
        user = TechskillsThree.objects.create(
           hours_per_day = data['hours_per_day'],
           preferred_time = data['preferred_time'],
           teaching_mode = data['teaching_mode'],
           how_long = data['how_long'],
           how_soon = data['how_soon'],
           starting_time = data['time_available'],
           days_available = data['days_available'],
         
        )
        return user    
      
class  LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = '__all__'    
    def create(self, data):
      user = Location.objects.create(
          home_address = data['home_address'],      
          region = data['region'],
          nearest_bus_stop = data['nearest_bus_stop'],
          state = data['state'],
    )
      return user
      
class TechSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechSkills
        fields = ['l_name', 'f_name', 'email', 'phone', 'parent_student']

    def validate(self, data):
        email = data.get('email')
        phone = data.get('phone')

        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email does not exist.")

        if not User.objects.filter(phone=phone).exists():
            raise serializers.ValidationError("Phone number does not exist.")
        
        return data
    def create(self,data):
      user = TechSkills.objects.create(
        parent_student = data['parent_student'],
        l_name = data['l_name'],
        f_name = data['f_name'],
        email = data['email'],
        phone = data['phone'],        
      ) 
      return user
 
class LanguageFirstSerializer(serializers.ModelSerializer):
    class Meta:
         model= LanguageFirstRequest
         fields='__all__'         
    def create(self, data):
        user = LanguageFirstRequest.objects.create(
          language = data ['language'],
          address = data ['address'],
          city = data ['city'],
          state = data ['state'],
          students = data ['students'],
          how_soon = data ['how_soon'],
        )
        return user
     
class LanguageLessonSerializer(serializers.ModelSerializer):
    class Meta:
         model= LanguageLesson
         fields='__all__'         
    def create(self, data):
        user = LanguageLesson.objects.create(
          days_available = data ['days_available'],
          program_duration = data ['program_duration'],
          hours_per_day = data ['hours_per_day'],
          start_time = data ['start_time'],
          student_level = data ['student_level'],
        )
        return user

class LanguageFormsubmissionSerializer(serializers.ModelSerializer):
    class Meta:
         model= LanguageFormSubmission
         fields='__all__'  
    def validate(self, data):
        email = data.get('email')
        phone = data.get('phone')

        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email does not exist.")

        if not User.objects.filter(phone=phone).exists():
            raise serializers.ValidationError("Phone number does not exist.")
        
        return data       
    def create(self, data):
        user = LanguageFormSubmission.objects.create(
          goal = data ['goal'],
          last_name = data ['last_name'],
          first_name = data ['first_name'],
          email = data['email'],
          phone = data ['phone'],
          preferred_gender = data ['preferred_gender'],
          teaching_mode = data ['teaching_mode'],
        )
        return user
         
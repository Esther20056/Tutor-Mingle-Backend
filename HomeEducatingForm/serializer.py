from rest_framework import serializers
from .models import Step1, AboutTheChild, Location, Step3, Retrieve

class Step1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Step1
        fields ='__all__'
    def create(self, data):
        user = Step1.objects.create(
         parent_student =data['parent_student'],       
         l_name = data['l_name'],
         f_name = data['f_name'],
         phoneNumber = data['phoneNumber'],
        )
        return user
    
class AboutTheChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutTheChild
        fields ='__all__'
    def create(self, data):
        user = AboutTheChild.objects.create(
         child_name =data['child_name'],       
         gender = data['gender'],
         child_class = data['child_class'],
         subject = data['subject'],
         goal = data['goal'],
         school_curriculum=data['school_curriculum'],
         tutor_gender=data['tutor_gender'],
         about_the_child=data['about_the_child'],
        )
        return user
class LocationSerializer(serializers.ModelSerializer):
       class Meta:
        model = Location
        fields ='__all__'
       def create(self, data):
         user = Location.objects.create(
         home_address=data['home_address'],
         region=data['region'],
         nearest_bus_stop=data['nearest_bus_stop'],
         state=data['state'],    
         )
         return user
class Step3Serializer(serializers.Serializer):
    class Meta:
        model = Step3
        field = '__all__'
    def create(self, data):
            user = Step3.objects.create( 
            days_available = data('days_available'),
            hours_per_day = data('hours_per_day'),   
            preferred_time = data('preferred_time'),  
            teaching_mode = data('teaching_mode'),  
            how_long = data('how_long'), 
            to_start_how_soon = data('to_start_how_soon')  
      )   

            return user       

class RetrieveSerializer(serializers.ModelSerializer):
    step1 = Step1Serializer()
    about_the_child = AboutTheChildSerializer()
    location = LocationSerializer()
    step3 = Step3Serializer()

    class Meta:
        model = Retrieve
        fields = '__all__'        
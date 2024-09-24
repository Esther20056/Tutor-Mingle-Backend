from rest_framework import serializers
from .models import AboutUser, SignUpTwo, User, SignUpThree, CapturedImage , TutoringExperience
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = '__all__'
                
    def validate(self, data):
        if not data.get('email'):
            raise serializers.ValidationError("Email is a required field")
        return data
      
    def create(self, data):
        pw = data['password']
        encrypted_pwd = make_password(pw, "wedrfghgfcdxsawsedrtyuuj")

        user = User.objects.create(
            email = data['email'], 
            phone = data['phone'],
            password = encrypted_pwd
        )
        return user

class AboutUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUser
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'birthday', 
            'nationality', 'gender', 'identification', 'profile', 
            'region', 'address', 'grade', 'degree', 'school_name', 
            'course', 'state', 'start_year', 'end_year'
        ]
    
    def validate(self, data):
        if not User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({"email": "Email does not exist."})
        if not User.objects.filter(phone=data['phone']).exists():
            raise serializers.ValidationError({"phone": "Phone does not exist."})
        return data

    def create(self, validated_data):
        email = validated_data['email']
        phone = validated_data['phone']
        
        try:
            user_instance = User.objects.get(email=email, phone=phone)
        except User.DoesNotExist:
            raise serializers.ValidationError({"non_field_errors": "User does not exist with provided email and phone."})
        about_user = AboutUser.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            birthday=validated_data['birthday'],
            nationality=validated_data['nationality'],
            gender=validated_data['gender'],
            identification=validated_data['identification'],  
            profile=validated_data['profile'], 
            region=validated_data['region'],
            address=validated_data['address'],
            grade=validated_data['grade'],
            degree=validated_data['degree'],
            school_name=validated_data['school_name'],
            course=validated_data['course'],
            state=validated_data['state'],
            start_year=validated_data['start_year'],
            end_year=validated_data['end_year'],
            user=user_instance
        )
        return about_user

class SignUpTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUpTwo
        fields = [
            'expert_subjects', 'years_of_experience', 'expertise_area', 
            'teaching_mode', 'time_available', 'days_available', 
            'preferred_online_tool', 'classes_you_teach'
        ]
    
    def create(self, validated_data):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            raise serializers.ValidationError("User must be authenticated to sign up.")
        
        user = request.user
        sign_up_two = SignUpTwo.objects.create(
            user=user,       
            expert_subjects=validated_data.get('expert_subjects'),
            years_of_experience=validated_data.get('years_of_experience'),
            expertise_area=validated_data.get('expertise_area'),
            time_available=validated_data.get('time_available'),
            teaching_mode=validated_data.get('teaching_mode'),
            days_available=validated_data.get('days_available'),
            preferred_online_tool=validated_data.get('preferred_online_tool'),
            classes_you_teach=validated_data.get('classes_you_teach')
        )
        return sign_up_two

class SignUpThreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUpThree
        fields ='__all__'
    def create(self, data):
        user = SignUpThree.objects.create(
         rate_for_tutoring_sessions =data['rate_for_tutoring_sessions'],       
         payment_options= data['payment_options'],
         terms_checkbox = data['terms_checkbox'],
         about_yourself = data['about_yourself'],
        )
        return user

class loginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError('Invalid credentials provided')

        return {
            'email': email,
            'user': user
        }

class CapturedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapturedImage
        fields = ('id', 'image', 'timestamp') 

class TutoringExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutoringExperience
        fields = '__all__'    
        
class UserDetailSerializer(serializers.ModelSerializer):
    about_users = serializers.SerializerMethodField()
    sign_up_two = serializers.SerializerMethodField()
    sign_up_three = serializers.SerializerMethodField()
    captured_images = serializers.SerializerMethodField()
    tutors_experience = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'about_users', 'sign_up_two', 'sign_up_three', 'captured_images', 'tutors_experience']

    def get_about_users(self, obj):
        about_users = AboutUser.objects.filter(user=obj)
        return AboutUserSerializer(about_users, many=True).data

    def get_sign_up_two(self, obj):
        sign_up_two = SignUpTwo.objects.filter(user=obj).first() 
        if sign_up_two:
            return SignUpTwoSerializer(sign_up_two).data
        return None
    
    
    def get_tutors_experience(self, obj):
        tutors_experience = TutoringExperience.objects.filter(user=obj).first() 
        if tutors_experience:
            return TutoringExperienceSerializer(tutors_experience).data
        return None

    def get_sign_up_three(self, obj):
        sign_up_three = SignUpThree.objects.filter(user=obj).first()  
        if sign_up_three:
            return SignUpThreeSerializer(sign_up_three).data
        return None

    def get_captured_images(self, obj):
        captured_images = CapturedImage.objects.filter(user=obj)  
        return CapturedImageSerializer(captured_images, many=True).data

from time import timezone
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from .managers import CustomUserManager
import datetime
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
import hashlib
import uuid

class User(AbstractUser):
    username = None
    first_name =None
    last_name =None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=17)
    last_login = models.DateTimeField(auto_now_add=True)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [] 

class AboutUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=18)
    birthday = models.DateField(default=datetime.date(2000, 1, 1))
    nationality = models.CharField(max_length=15)
    STATE_CHOICES = [
        ('Abia', 'Abia'),
        ('Adamawa', 'Adamawa'),
        ('Akwa Ibom', 'Akwa Ibom'),
        ('Anambra', 'Anambra'),
        ('Bauchi', 'Bauchi'),
        ('Bayelsa', 'Bayelsa'),
        ('Benue', 'Benue'),
        ('Borno', 'Borno'),
        ('Cross River', 'Cross River'),
        ('Delta', 'Delta'),
        ('Ebonyi', 'Ebonyi'),
        ('Edo', 'Edo'),
        ('Ekiti', 'Ekiti'),
        ('Enugu', 'Enugu'),
        ('Gombe', 'Gombe'),
        ('Imo', 'Imo'),
        ('Jigawa', 'Jigawa'),
        ('Kaduna', 'Kaduna'),
        ('Kano', 'Kano'),
        ('Katsina', 'Katsina'),
        ('Kebbi', 'Kebbi'),
        ('Kogi', 'Kogi'),
        ('Kwara', 'Kwara'),
        ('Lagos', 'Lagos'),
        ('Nasarawa', 'Nasarawa'),
        ('Niger', 'Niger'),
        ('Ogun', 'Ogun'),
        ('Ondo', 'Ondo'),
        ('Osun', 'Osun'),
        ('Oyo', 'Oyo'),
        ('Plateau', 'Plateau'),
        ('Rivers', 'Rivers'),
        ('Sokoto', 'Sokoto'),
        ('Taraba', 'Taraba'),
        ('Yobe', 'Yobe'),
        ('Zamfara', 'Zamfara'),
    ]   
    state = models.CharField(max_length=100, choices=STATE_CHOICES)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    identification = models.ImageField(upload_to='Images')
    profile = models.ImageField(upload_to='Images')
    region = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    GRADE_CHOICES = [
        ("Not Applicable", "Not Applicable"),
        ("Pass Degree", "Pass Degree"),
        ("Third Class", "Third Class"),
        ("Lower Second Class", "Lower Second Class"),
        ("Upper Second Class", "Upper Second Class"),
        ("Distinction", "Distinction"),
        ("First Class", "First Class"),
    ]
    grade = models.CharField(max_length=35, choices=GRADE_CHOICES)
    DEGREE_CHOICES = [
        ("Post Graduate Diploma in Education (PGDE)", "Post Graduate Diploma in Education (PGDE)"),
        ("Ordinary National Diploma (OND)", "Ordinary National Diploma (OND)"),
        ("National Certificate of Education (NCE)", "National Certificate of Education (NCE)"),
        ("Master of Science (M.Sc)", "Master of Science (M.Sc)"),
        ("Master of Laws (LL.M)", "Master of Laws (LL.M)"),
        ("Master of Education (M.Ed)", "Master of Education (M.Ed)"),
        ("Master of Business Administration (MBA)", "Master of Business Administration (MBA)"),
        ("Master of Art (MA)", "Master of Art (MA)"),
        ("Higher National Diploma (HND)", "Higher National Diploma (HND)"),
        ("Doctor of Philosophy (PhD)", "Doctor of Philosophy (PhD)"),
        ("Doctor of Medicine (MD)", "Doctor of Medicine (MD)"),
        ("Doctor of Education (Ed.D)", "Doctor of Education (Ed.D)"),
        ("Diploma Certificate (Dipl.)", "Diploma Certificate (Dipl.)"),
        ("Bachelor of Medicine and Surgery (MBBS)", "Bachelor of Medicine and Surgery (MBBS)"),
        ("Bachelor of Science (B.Sc)", "Bachelor of Science (B.Sc)"),
        ("Bachelor of Technology (B.Tech)", "Bachelor of Technology (B.Tech)"),
        ("Bachelor of Laws (LL.B)", "Bachelor of Laws (LL.B)"),
        ("Bachelor of Engineering (B.Eng)", "Bachelor of Engineering (B.Eng)"),
        ("Bachelor of Education (B.Ed)", "Bachelor of Education (B.Ed)"),
        ("Bachelor of Arts (B.A)", "Bachelor of Arts (B.A)"),
    ]
    degree = models.CharField(max_length=130, choices=DEGREE_CHOICES)
    school_name = models.CharField(max_length=80)
    start_year = models.DateField(default=datetime.date(2000, 1, 1))
    end_year = models.DateField(default=datetime.date(2000, 1, 1))
    COURSE_CHOICES = [
        ("Biological and Physical Sciences", "Biological and Physical Sciences"),
        ("Engineering and Technology", "Engineering and Technology"),
        ("Medical, Nursing and Clinical Sciences", "Medical, Nursing and Clinical Sciences"),
        ("Languages, Linguistics and Communication", "Languages, Linguistics and Communication"),
        ("Design and Architecture", "Design and Architecture"),
        ("Social Sciences, History and Law", "Social Sciences, History and Law"),
        ("Arts, Music, and Humanities", "Arts, Music, and Humanities"),
        ("Business, Finance and Administration", "Business, Finance and Administration"),
        ("Education - Math, Technology and Sciences", "Education - Math, Technology and Sciences"),
        ("Education - Art, Development and Humanities", "Education - Art, Development and Humanities"),
        ("Education - Counselling, Special Needs, General", "Education - Counselling, Special Needs, General"),
        ("Education - Business and Management", "Education - Business and Management"),
    ]
    course = models.CharField(max_length=130, choices=COURSE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="reguser")

class SignUpTwo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sign_up_details')
    expert_subjects = models.CharField(max_length=50)
    years_of_experience = models.CharField(max_length=15)
    expertise_area = models.CharField(max_length=90)
    TEACHING_MODE_CHOICES = [
        ('Online', 'Online'),
        ('Physical', 'Physical'),
        ('Both', 'Both'),
    ]
    teaching_mode = models.CharField(max_length=8, choices=TEACHING_MODE_CHOICES)
    time_available = models.JSONField()
    days_available = models.JSONField()
    preferred_online_tool = models.CharField(max_length=15, blank=True)
    classes_you_teach = models.CharField(max_length=200)

class EmailVerificationToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    expired_at = models.DateTimeField()
    
class SignUpThree(models.Model):
   rate_for_tutoring_sessions = models.DecimalField(max_digits=10, decimal_places=2, default=settings.DEFAULT_CURRENCY)
   PAYMENTOPTIONS_CHOICES = [
        ('Cash', 'Cash'),
        ('Transfer', 'Transfer'),
    ]
   payment_options = models.CharField(max_length=10, choices=PAYMENTOPTIONS_CHOICES)    
   terms_checkbox = models.BooleanField(default=False)
   about_yourself = models.TextField(max_length=500, default='')
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='signup_user')
    
class login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)    
    
class CapturedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_image')
    
class TutoringExperience(models.Model):
    has_work_experience = models.BooleanField(default=False)
    no_work_experience = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_experience')
    
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_address = models.CharField(max_length=255, blank=True, null=True)
    company_phone_number = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return self.company_name if self.company_name else 'No Company'
    

class PasswordResetRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def is_expired(self):
        return timezone.now() > self.expires_at

    def generate_token(self):
        token_str = get_random_string(64)
        self.token = hashlib.sha256(token_str.encode()).hexdigest()

    @classmethod
    def create_request(cls, user):
        instance = cls(user=user)
        instance.generate_token()
        instance.expires_at = timezone.now() + timezone.timedelta(hours=1)
        instance.save()
        reset_link = f"http://localhost:8000/reset/{instance.token}/"
        send_mail(
            "Password Reset Request",
            f"Click the following link to reset your password: {reset_link}",
            "helo@example.com",
            [user.email],
            fail_silently=False,
        )
        return instance
    
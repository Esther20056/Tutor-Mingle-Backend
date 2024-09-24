from django.db import models

class TechSkills(models.Model):
    PARENT_STUDENT_CHOIECS = [
        ("Parent", "Parent"),
        ("Student", "Student")
    ]
    parent_student = models.CharField(max_length=9, choices=PARENT_STUDENT_CHOIECS) 
    l_name = models.CharField(max_length=20) 
    f_name = models.CharField(max_length=20) 
    email = models.CharField(max_length=30, unique=True) 
    phone = models.CharField(max_length=18)

class TechSkillsTwo(models.Model):
    child_name = models.CharField(max_length=30)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.CharField(max_length=8)
    COURSE_CHOICES = [
        ('UI/UX','UI/UX'),
        ('Front-end Development','Front-end Development'),
        ('Back-end Development','Back-end Development'),
        ('iOS and Android Development','iOS and Android Development'),
    ]
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    GOAL_CHOICES =[
        ('Develop interactive apps for educational use', 'Develop interactive apps for educational use'),
        ('Master coding fundamentals for app creation', 'Master coding fundamentals for app creation'),
        ('Create engaging UI/UX for diverse audiences', 'Create engaging UI/UX for diverse audiences'),
        ('Learn to integrate multimedia for impact', 'Learn to integrate multimedia for impact'),
        ('Build apps fostering learning and play', 'Build apps fostering learning and play'),
        ('Understand app deployment and maintenance basics', 'Understand app deployment and maintenance basics'),
    ]
    goal = models.CharField(max_length=80, choices=GOAL_CHOICES)
    TUTOR_GENDER_CHOIECS = [
        ('Male','Male'),
        ('Female','Female'),
        ('Any gender is fine', 'Any gender is fine'),
    ]
    tutor_gender =models.CharField(max_length=19, choices=TUTOR_GENDER_CHOIECS)
    about_the_child = models.CharField(max_length=255)
    user = models.ForeignKey(TechSkills, on_delete=models.CASCADE, related_name='user')

class TechskillsThree(models.Model):
    hours_per_day = models.CharField(max_length=15)
    PREFERRED_TIME_CHOICES = [
        ('Evening', 'Evening'),
        ('Afternoon', 'Afternoon'),
    ]
    preferred_time = models.CharField(max_length=12, choices=PREFERRED_TIME_CHOICES)
    TEACHINGMODE_CHOICES=[
        ('Online', 'Online'),
        ('Physical', 'Physical'),
    ]
    teaching_mode = models.CharField(max_length=8, choices=TEACHINGMODE_CHOICES) 
    HOW_LONG_CHOICES = [
        ('1 Week', '1 Week'),
        ('2 Weeks', '2 Weeks'),
        ('3 Weeks', '3 Weeks'),
        ('4 Weeks', '4 Weeks'),
        ('Monthly', 'Monthly'),
    ]
    how_long = models.CharField(max_length=10, choices=HOW_LONG_CHOICES)
    TO_START_HOW_SOON_CHOICES = [
        ('In a few days', 'In a few days'),
        ('Immediately', 'Immediately'),
        ('In a few weeks', 'In a few weeks'),
    ]
    starting_time = models.CharField(max_length=9, default=1)
    user = models.ForeignKey(TechSkills, on_delete=models.CASCADE, related_name='about_users')
    days_available = models.JSONField()

class Location(models.Model):
    home_address = models.CharField(max_length=40)
    region = models.CharField(max_length=30)
    nearest_bus_stop = models.CharField(max_length=60)
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
    state = models.CharField(max_length=30, choices=STATE_CHOICES)
    user = models.ForeignKey(TechSkills, on_delete=models.CASCADE, related_name='locations')

class LanguageFirstRequest(models.Model):
    LANGUAGE_CHOICES = [
        ('Yoruba', 'Yoruba'),
        ('Igbo', 'Igbo'),
        ('French', 'French'),
        ('Hausa', 'Hausa'),
        ('German', 'German'),
        ('Spanish', 'Spanish'),
        ('Arabic', 'Arabic'),
        ('Chinese', 'Chinese'),
    ]    
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
    HOW_SOON_CHOICES = [
        ('Immediately', 'Immediately'),
        ('In a few days', 'In a few days'),
        ('In a few weeks', 'In a few weeks'),
    ]    
    STUDENT_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    students = models.CharField(max_length=1, choices=STUDENT_CHOICES)
    how_soon = models.CharField(max_length=50, choices=HOW_SOON_CHOICES)

class LanguageLesson(models.Model):
    PROGRAM_DURATION_CHOICES = [
        ('1 Week', '1 Week'),
        ('2 Weeks', '2 Weeks'),
        ('3 Weeks', '3 Weeks'),
        ('4 Weeks', '4 Weeks'),
        ('Monthly', 'Monthly'),
    ]
    HOURS_PER_DAY_CHOICES = [
        ('1 hour', '1 hour'),
        ('1 hour 30 minutes', '1 hour 30 minutes'),
        ('2 hours', '2 hours'),
        ('2 hours 30 minutes', '2 hours 30 minutes'),
        ('3 hours', '3 hours'),
        ('4 hours', '4 hours'),
    ]
    days_available = models.JSONField()
    program_duration = models.CharField(max_length=20, choices=PROGRAM_DURATION_CHOICES)
    hours_per_day = models.CharField(max_length=20, choices=HOURS_PER_DAY_CHOICES)
    start_time = models.CharField(max_length=10)
    student_level = models.CharField(max_length=100)
    user = models.ForeignKey(LanguageFirstRequest, on_delete=models.CASCADE)

class LanguageFormSubmission(models.Model):
    goal = models.TextField()
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    preferred_gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('A', 'Any Gender')])
    teaching_mode = models.CharField(max_length=10, choices=[('Physical', 'Physical'), ('Online', 'Online')])
    user = models.ForeignKey(LanguageLesson, on_delete=models.CASCADE)


        
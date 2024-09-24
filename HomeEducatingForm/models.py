from django.db import models


class Step1(models.Model):
    PARENT_STUDENT_CHOICES = [
        ("Parent", "Parent"),
        ("Student", "Student")
    ]
    parent_student = models.CharField(max_length=9, choices=PARENT_STUDENT_CHOICES)
    l_name = models.CharField(max_length=20)
    f_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30, unique=True)
    phoneNumber = models.CharField(max_length=18)

class AboutTheChild(models.Model):
    user = models.ForeignKey(Step1, on_delete=models.CASCADE)
    child_name = models.CharField(max_length=30)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    CLASS_CHOICES = [
        ('Preschool', 'Preschool'),
        ('Nursery 1', 'Nursery 1'),
        ('Nursery 2', 'Nursery 2'),
        ('Elementary 1', 'Elementary 1'),
        ('Elementary 2', 'Elementary 2'),
        ('Elementary 3', 'Elementary 3'),
        ('Elementary 4', 'Elementary 4'),
        ('Elementary 5', 'Elementary 5'),
        ('Elementary 6', 'Elementary 6'),
        ('Grade 7', 'Grade 7'),
        ('Grade 8', 'Grade 8'),
        ('Grade 9', 'Grade 9'),
        ('Grade 10', 'Grade 10'),
        ('Grade 11', 'Grade 11'),
        ('Grade 12', 'Grade 12'),
    ]
    child_class = models.CharField(max_length=13, choices=CLASS_CHOICES)
    subject = models.CharField(max_length=50)
    GOAL_CHOICES = [
        ('WAEC/ NECO/ UME/ JUPEB', 'WAEC/ NECO/ UME/ JUPEB'),
        ('Primary School Leaving Certificate Examination (PSLCE)', 'Primary School Leaving Certificate Examination (PSLCE)'),
        ('Basic Education Certificate Examination (BECE)', 'Basic Education Certificate Examination (BECE)'),
        ('National Common Entrance Examination (NCEE)', 'National Common Entrance Examination (NCEE)'),
        ('Homework/ Revision/ Study help', 'Homework/ Revision/ Study help'),
    ]
    goal = models.CharField(max_length=80, choices=GOAL_CHOICES)
    SCHOOL_CURRICULUM_CHOICES = [
        ('Nigerian', 'Nigerian'),
        ('American', 'American'),
        ('British', 'British'),
        ('Not sure', 'Not sure'),
    ]
    school_curriculum = models.CharField(max_length=10, choices=SCHOOL_CURRICULUM_CHOICES)
    TUTOR_GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Any gender is fine', 'Any gender is fine'),
    ]
    tutor_gender = models.CharField(max_length=19, choices=TUTOR_GENDER_CHOICES)
    about_the_child = models.CharField(max_length=255)

class Location(models.Model):
    user = models.ForeignKey(Step1, on_delete=models.CASCADE)
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
    state = models.CharField(max_length=100, choices=STATE_CHOICES)

class Step3(models.Model):
    user = models.ForeignKey(Step1, on_delete=models.CASCADE)
    days_available = models.JSONField()
    HOURS_PER_DAY_CHOICES = [
        ('One hour', 'One hour'),
        ('Two hours', 'Two hours'),
        ('Three hours', 'Three hours'),
        ('Four hours', 'Four hours'),
        ('Five hours', 'Five hours'),
    ]
    hours_per_day = models.CharField(max_length=12, choices=HOURS_PER_DAY_CHOICES)
    PREFERRED_TIME_CHOICES = [
        ('11:00am', '11:00am'),
        ('11:30am', '11:30am'),
        ('12:00pm', '12:00pm'),
        ('12:30pm', '12:30pm'),
        ('1:00pm', '1:00pm'),
        ('1:30pm', '1:30pm'),
        ('2:00pm', '2:00pm'),
        ('2:30pm', '2:30pm'),
        ('3:00pm', '3:00pm'),
        ('3:30pm', '3:30pm'),
        ('4:00pm', '4:00pm'),
        ('4:30pm', '4:30pm'),
        ('5:00pm', '5:00pm'),
        ('5:30pm', '5:30pm'),
    ]
    preferred_time = models.CharField(max_length=9, choices=PREFERRED_TIME_CHOICES)
    TEACHING_MODE_CHOICES = [
        ('Online', 'Online'),
        ('Physical', 'Physical'),
    ]
    teaching_mode = models.CharField(max_length=8, choices=TEACHING_MODE_CHOICES)
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
    to_start_how_soon = models.CharField(max_length=20, choices=TO_START_HOW_SOON_CHOICES)

class Retrieve(models.Model):
    step1 = models.OneToOneField(Step1, on_delete=models.CASCADE)
    about_the_child = models.OneToOneField(AboutTheChild, on_delete=models.CASCADE)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    step3 = models.OneToOneField(Step3, on_delete=models.CASCADE)
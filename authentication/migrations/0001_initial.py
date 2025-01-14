# Generated by Django 5.1 on 2024-08-23 15:14

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=17)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AboutUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=18)),
                ('birthday', models.DateField(default=datetime.date(2000, 1, 1))),
                ('nationality', models.CharField(max_length=15)),
                ('state', models.CharField(choices=[('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa Ibom', 'Akwa Ibom'), ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross River', 'Cross River'), ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'), ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo'), ('Plateau', 'Plateau'), ('Rivers', 'Rivers'), ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara')], max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('identification', models.ImageField(upload_to='Images')),
                ('profile', models.ImageField(upload_to='Images')),
                ('region', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=40)),
                ('grade', models.CharField(choices=[('Not Applicable', 'Not Applicable'), ('Pass Degree', 'Pass Degree'), ('Third Class', 'Third Class'), ('Lower Second Class', 'Lower Second Class'), ('Upper Second Class', 'Upper Second Class'), ('Distinction', 'Distinction'), ('First Class', 'First Class')], max_length=35)),
                ('degree', models.CharField(choices=[('Post Graduate Diploma in Education (PGDE)', 'Post Graduate Diploma in Education (PGDE)'), ('Ordinary National Diploma (OND)', 'Ordinary National Diploma (OND)'), ('National Certificate of Education (NCE)', 'National Certificate of Education (NCE)'), ('Master of Science (M.Sc)', 'Master of Science (M.Sc)'), ('Master of Laws (LL.M)', 'Master of Laws (LL.M)'), ('Master of Education (M.Ed)', 'Master of Education (M.Ed)'), ('Master of Business Administration (MBA)', 'Master of Business Administration (MBA)'), ('Master of Art (MA)', 'Master of Art (MA)'), ('Higher National Diploma (HND)', 'Higher National Diploma (HND)'), ('Doctor of Philosophy (PhD)', 'Doctor of Philosophy (PhD)'), ('Doctor of Medicine (MD)', 'Doctor of Medicine (MD)'), ('Doctor of Education (Ed.D)', 'Doctor of Education (Ed.D)'), ('Diploma Certificate (Dipl.)', 'Diploma Certificate (Dipl.)'), ('Bachelor of Medicine and Surgery (MBBS)', 'Bachelor of Medicine and Surgery (MBBS)'), ('Bachelor of Science (B.Sc)', 'Bachelor of Science (B.Sc)'), ('Bachelor of Technology (B.Tech)', 'Bachelor of Technology (B.Tech)'), ('Bachelor of Laws (LL.B)', 'Bachelor of Laws (LL.B)'), ('Bachelor of Engineering (B.Eng)', 'Bachelor of Engineering (B.Eng)'), ('Bachelor of Education (B.Ed)', 'Bachelor of Education (B.Ed)'), ('Bachelor of Arts (B.A)', 'Bachelor of Arts (B.A)')], max_length=130)),
                ('school_name', models.CharField(max_length=80)),
                ('start_year', models.DateField(default=datetime.date(2000, 1, 1))),
                ('end_year', models.DateField(default=datetime.date(2000, 1, 1))),
                ('course', models.CharField(choices=[('Biological and Physical Sciences', 'Biological and Physical Sciences'), ('Engineering and Technology', 'Engineering and Technology'), ('Medical, Nursing and Clinical Sciences', 'Medical, Nursing and Clinical Sciences'), ('Languages, Linguistics and Communication', 'Languages, Linguistics and Communication'), ('Design and Architecture', 'Design and Architecture'), ('Social Sciences, History and Law', 'Social Sciences, History and Law'), ('Arts, Music, and Humanities', 'Arts, Music, and Humanities'), ('Business, Finance and Administration', 'Business, Finance and Administration'), ('Education - Math, Technology and Sciences', 'Education - Math, Technology and Sciences'), ('Education - Art, Development and Humanities', 'Education - Art, Development and Humanities'), ('Education - Counselling, Special Needs, General', 'Education - Counselling, Special Needs, General'), ('Education - Business and Management', 'Education - Business and Management')], max_length=130)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='reguser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

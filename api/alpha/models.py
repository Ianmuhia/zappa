from __future__ import unicode_literals
from django.db import models
# from django.contrib.auth.models import User
from django.http import request
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.conf import settings
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

GENDER_CHOICES = (
    ('F', 'F'),
    ('M', 'M'),
)
A = 'a'
B = 'b'
C = 'c'
D = 'd'
GRADE_CHOICES =(
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D'),
    )

COURSE_CHOICES =(
    ('CERTIFICATE','CERTIFICATE'),
    ('DIPLOMA','DIPLOMA'),
    ('BACHELORS','BACHELORS'),
    ('SHORT COURSE','SHORT COURSE'),
    )


# User = get_user_model()

class Post(models.Model):
    title = models.TextField(max_length = 50, null = False)
    posted_time = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length = 1000, null = False)
    image = models.ImageField(null=True, blank=True)
    user = models.OneToOneField('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post_details', kwargs={'pk': self.pk})


class Notification(models.Model):
    title = models.TextField(max_length = 50, null = False, default='')
    text = models.TextField(max_length = 1500, null = True)
    image = models.ImageField(null=True, blank=True)
    pdf_file = models.FileField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('notification_details', kwargs={'pk': self.pk})
    
class Library(models.Model):
    title = models.TextField(max_length=20, null=False)
    pdf_file = models.FileField(null=False)


class CustomUser(AbstractBaseUser):
    is_teacher = models.BooleanField(default=False, verbose_name= 'Teacher')
    is_student = models.BooleanField(default=False, verbose_name= 'Student')
    first_name = models.CharField(max_length=20, null=False, default='')
    sir_name = models.CharField(max_length=20, null=False, default='')
    image = models.ImageField(null=False, blank=False)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=1, blank=False)
    class Meta:
        unique_together = ("gender", "first_name", "last_name", "image")
        db_table = 'custom_users'
        
        
class Student(models.Model):
    user = models.OneToOneField(settings.REST_AUTH_REGISTER_SERIALIZERS, on_delete=models.CASCADE, primary_key=True)
    registration_number = models.CharField(max_length=20, null=False, unique=True)
    # username = None
    # password = None
    # grade = selectMultipleField( max_length =4, choices=GRADE_CHOICES)
    course = models.CharField(choices=COURSE_CHOICES,max_length=15, blank=False, default='')
    year = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)], default = 1, verbose_name='Year')
    
    class Meta:
        db_table = "students"
        
class StudentSignUp(UserCreationForm):
    registration_number = forms.CharField(max_length=50, required = True )
    year = forms.models.IntegerField(min_value = 1, max_value=6, required=True, label=_('Year'))
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'registration_number',
            'year'
        )
@transaction.atomic
def save(self):
    user = super(StudentSignUp, self).save(commit=False)
    user.is_student = True
    user.save()
    Student.objects.create(
        user=user,
        year=self.cleaned_data.get('year'),
        registration_number =self.cleaned_data.get('registration_number')
    )
    return user


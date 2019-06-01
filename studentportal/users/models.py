from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from courses.models import Course


# Create your models here.
class User(AbstractUser):
    STUDENT = 1
    TUTOR = 2
    STAFF = 3
    ROLE_CHOICES = (
        (STUDENT, 'student'),
        (TUTOR, 'tutor'),
        (STAFF, 'staff'),
    )
    date_of_birth = models.DateField(null=True)
    contact_no = PhoneNumberField(null=True)
    place = models.CharField(max_length=20, null=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True)


class Staff(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=20)


class Tutor(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_study')

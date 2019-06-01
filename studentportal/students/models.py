import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.models import User
from users.models import Tutor
from courses.models import Course
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


# Create your models here.

class Student(models.Model):

    FEMALE = 'F'
    MALE = 'M'
    GENDER_OPTIONS = (
        (FEMALE, 'female'),
        (MALE, 'male')
    )

    user_profile = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS)
    date_of_joining = models.DateField(default=datetime.date.today)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='student')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='student')
    father_name = models.CharField(max_length=30,)
    location = models.CharField(max_length=30,)
    address = models.TextField()
    add_phone = PhoneNumberField(null=True)


class Payment(models.Model):
    FULL_PAYMENT = 'F'
    INSTALL_PAYMENT = 'I'
    PAYMENT_OPTION = (
        (FULL_PAYMENT, 'full'),
        (INSTALL_PAYMENT, 'installment')
    )
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    payment_mode = models.CharField(max_length=1, choices=PAYMENT_OPTION)
    amount_paid = models.PositiveIntegerField()

    def add_amount(self, amount=0):
        self.amount_paid += amount
        self.save()


class Academic(models.Model):
    student_details = models.OneToOneField(Student, on_delete=models.CASCADE)
    qualification = models.CharField('Qualification', max_length=20)
    institute = models.CharField('University/Institute', max_length=30)
    year_of_passing = models.IntegerField('Year of passing',
                                          validators=[MaxValueValidator(datetime.date.today().year),
                                                      MinValueValidator(1960)])
    major_subject = models.CharField('Major subject', max_length=40)

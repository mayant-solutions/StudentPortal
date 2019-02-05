import datetime

from django.db import models
from studentportal.users.models import User


# Create your models here.
class Student(User):
    date_of_joining = models.DateField(default=datetime.date.today)


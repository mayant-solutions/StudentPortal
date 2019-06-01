from django.db import models
# from tutors.models import Tutor
# Create your models here.


class Technology(models.Model):
    name = models.CharField(max_length=15)


class Course(models.Model):
    name = models.CharField('Name', max_length=30)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE,
                                   related_name='courses')
    tutor = models.ForeignKey('users.Tutor', on_delete=models.PROTECT,
                              related_name='tutor_teaching')
    fee = models.PositiveIntegerField()
    hours = models.PositiveIntegerField()

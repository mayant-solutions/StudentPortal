from django.db import models
from django.utils.timezone import now
from users.models import Tutor
from students.models import Student


# Create your models here.

class Assignment(models.Model):

    BLOG = 'B'
    PROGRAM = 'C'
    PRESENTATION = 'P'
    OTHER = 'O'

    ASSIGNMENT_CHOICE = (
        (BLOG, 'blog'),
        (PROGRAM, 'program'),
        (PRESENTATION, 'presentation'),
        (OTHER, 'other'),

    )
    head = models.CharField('Captions', max_length=200)
    content = models.TextField('Content')
    time_created = models.DateTimeField(default=now)
    type = models.CharField(max_length=1, choices=ASSIGNMENT_CHOICE)
    created_by = models.OneToOneField(Tutor, on_delete=models.PROTECT)
    student = models.ManyToManyField(Student)
    # file = models.FileField()





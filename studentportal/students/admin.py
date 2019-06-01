from django.contrib import admin
from .models import Student, Payment, Academic
# Register your models here.
admin.site.register(Student)
admin.site.register(Academic)
admin.site.register(Payment)
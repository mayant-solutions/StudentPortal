from django.contrib import admin
from .models import User, Tutor, Staff
# Register your models here.
admin.site.register(User)
admin.site.register(Staff)
admin.site.register(Tutor)
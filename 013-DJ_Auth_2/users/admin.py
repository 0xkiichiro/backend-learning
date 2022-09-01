from django.contrib import admin
from .models import User
from .models import UserProfile
# Register your models here.
admin.site.register(UserProfile)
# admin.site.register(User)
from django.contrib import admin
from basic_app.models import UserProfileInfo

# Register your models here.
# class UserProfileInfoAdmin(admin.ModelAdmin):
# 	list_display = ['username', 'email', 'password', 'portfolio_site', 'profile_pic']


admin.site.register(UserProfileInfo)



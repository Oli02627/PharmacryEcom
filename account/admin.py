from django.contrib import admin
from .models import User, Customer


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id','username','first_name','last_name','email']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'name','address','city','state','zip_code']
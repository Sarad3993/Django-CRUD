from django.contrib import admin
from appcrud.models import *


class StudentsAdmin(admin.ModelAdmin):
    list_display = ['name','address','email','contact']


admin.site.register(Students,StudentsAdmin)

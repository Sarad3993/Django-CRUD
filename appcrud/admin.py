from django.contrib import admin
from appcrud.models import *


class StudentsAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email']


admin.site.register(Students,StudentsAdmin)

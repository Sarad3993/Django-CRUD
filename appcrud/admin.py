from django.contrib import admin
from appcrud.models import *


class StudentsAdmin(admin.ModelAdmin):
    list_display = ['name','address','email','contact','image_tag']


admin.site.register(Students,StudentsAdmin)

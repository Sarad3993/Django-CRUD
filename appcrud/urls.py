from django.urls import path
from appcrud.views import *

app_name = 'appcrud'

urlpatterns = [
    path('',index,name='index'),
    path('read_student',read_student,name='read_student'),
    path('add_student',add_student,name='add_student'),
    path('update_student/<int:id>',update_student,name='update_student'),
    path('delete_student/<int:id>',delete_student,name='delete_student')
]

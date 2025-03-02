
from django.urls import path

from configapp.views import *

urlpatterns = [
    path('fanlar/<int:fan_id>',get_fanlar,name='get_fanlar'),
    path('add_fanlar/',add_fanlar,name='add_fanlar'),
    path('add_student/',add_student,name='add_student'),
    path('generate_pdf/<int:student_id>/',generate_pdf,name='generate_pdf'),

]

from Apps.firstapp.models import Grades, Students
from django.utils import timezone
from datetime import *

grade1 = Grades.objects.get(pk=1)
stu = Students.objects.get(pk=1)

grade1.students_set_all() #班级下所有学生
# 直接新建班级里的学生
stu3 = grade1.students_set_create(s_name=u"", s_age="") #注意中文需要加u 转码


# python manage.py makemigrations
# python manage.py migrate

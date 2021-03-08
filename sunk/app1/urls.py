from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(\d+)/(\d+)/$', views.num),
    url(r'^grades/$', views.grades),
    url(r'^grades/(\d+)$', views.gradesStudents),
    url(r'^students/$', views.students)

]
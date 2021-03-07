from django.db import models


# Create your models here.

class Grades(models.Model):
    g_name = models.CharField(max_length=20)
    g_date = models.DateField()
    g_girl_num = models.IntegerField()
    g_boy_num = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.g_name


class Students(models.Model):
    s_name = models.CharField(max_length=20)
    s_gender = models.BooleanField(default=True)
    s_age = models.IntegerField()
    s_contend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    s_grade = models.ForeignKey("Grades", on_delete=models.CASCADE)
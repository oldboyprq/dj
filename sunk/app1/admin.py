from django.contrib import admin

# Register your models here.
from .models import Grades, Students


# 注册
class StundentsInfo(admin.TabularInline):  # admin.StackedInline
    model = Students
    extra = 2


class GradesAdmin(admin.ModelAdmin):
    inlines = [StundentsInfo]
    # 列表页属性
    list_display = ['pk', 'g_name', 'g_date', 'g_girl_num', 'g_boy_num', 'isDelete']  # 显示字段
    list_filter = ['g_name']  # 过滤字段
    search_fields = ['g_name']  # 查找字段
    list_per_page = 5  # 每页显示数量

    # 添加、修改页属性
    # fields = ['g_girl_num', 'g_boy_num', 'g_name', 'g_date', 'isDelete']   # 属性的先后顺序
    fieldsets = [
        ("num", {"fields": ['g_boy_num', 'g_girl_num']}),
        ("base", {"fields": ['g_name', 'g_date', 'isDelete']})
    ]  # 属性分类 与fields 不能同时使用


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.s_gender:
            return "男"
        else:
            return "女"
    gender.short_description = "性别"  # 设置页面列的名称
    list_display = ['pk', 's_name', 's_age', gender, 's_contend', 'isDelete', 's_grade']
    list_filter = ['s_grade']
    list_per_page = 2
    search_fields = ['s_name']
    # 执行动作的位置
    actions_on_top = False
    actions_on_bottom = True

admin.site.register(Grades, GradesAdmin)

# admin.site.register(Students,StudentsAdmin)

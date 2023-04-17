from django.contrib import admin
from .models import Student,Job,Employee,Department,DeptEmp,details

# Register your models here.
# admin.site.register(Student)
# admin.site.register(Job)

@admin.register(Student)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','name','mobile','password','email']
    
    
@admin.register(Job)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','job','salary']
    

@admin.register(details)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','emp_name','salary']

@admin.register(Employee)
class UserAdmin(admin.ModelAdmin):
    list_display=['first_name']
    
@admin.register(Department)
class UserAdmin(admin.ModelAdmin):
    list_display=['dept_no','dept_name']
    
@admin.register(DeptEmp)
class UserAdmin(admin.ModelAdmin):
    list_display=['emp_no','dept_no']
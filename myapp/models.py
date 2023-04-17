from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=23)
    email=models.EmailField()
    password=models.CharField(max_length=32)
    mobile=models.CharField(max_length=34)
    # product_rank = models.OneToOneField(Job,on_delete=models.CASCADE)

    def __str__(self):
        # return self.mobile
        return str(self.id)
    
    class Meta:
        db_table='student_table'


class Job(models.Model):
    job=models.ForeignKey(Student,on_delete=models.CASCADE)
    salary=models.CharField(max_length=34)

    def __str__(self):
        return self.salary
    
class details(models.Model):
    emp_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    salary = models.ForeignKey(Job, on_delete=models.CASCADE)   

    


class Employee(models.Model):
    emp_no = models.IntegerField(primary_key=True)
    first_name =models.CharField( max_length=4)
    last_name =models.CharField( max_length=4)
    
    def __str__(self):
        return self.first_name


class Department(models.Model):
    dept_no = models.CharField(primary_key=True, max_length=4)
    dept_name = models.CharField(unique=True, max_length=40)
    
    def __str__(self):
        return self.dept_name

class DeptEmp(models.Model):
    emp_no = models.ForeignKey(Employee, on_delete=models.CASCADE)
    dept_no = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    





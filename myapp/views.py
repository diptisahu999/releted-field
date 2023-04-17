from django.shortcuts import render,redirect
from .models import Student,Job,Employee,Department,DeptEmp,details
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    if request.method=='GET':
        return render(request,'index.html')
    else:
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password'],
            mobile=request.POST['mobile'],
        )
        return redirect('show')
    

def show(request):
    sss=details.objects.all().select_related('emp_name').select_related('salary')
    free={
        'sss':sss
    }
    return render(request,'in.html',free)


def delete(request,pk):
    # Student.objects.filter(id=pk).delete()
    Student.objects.get(id=pk).delete()
    return redirect('show')


def edit(request,pk):
    ss=Student.objects.get(id=pk)
    if request.method=='POST':
        ss.name=request.POST['name']
        ss.email=request.POST['email']
        ss.password=request.POST['password']
        ss.mobile=request.POST['mobile']

        ss.save()
        return redirect('show')
    
    return render(request,'edit.html',{'pob':ss})


def log_page(request):
    if request.method=='POST':
        user=request.POST.get('username')
        upass=request.POST.get('password')
        print(user,upass)
        
        return render(request,'edit.html')
    
    
# def ss(request):
#     # d=Student.objects.filter(id=9).select_related()
#     # book = Job.objects.select_related('job').get(id=8)
#     # d=book.job.name,book.job.email,book.job.password
#     # print(d)
#     # d=Student.objects.order_by("name").values_list("name",flat=True)   # all name get in a list
   
#     return render(request,'join.html',{'d':d})


def s(request):
    # abc = DeptEmp.objects.all().select_related('emp_no').select_related('dept_no')
    # abc = details.objects.filter(id=2).select_related('emp_name').select_related('salary')  # single data get 
    abc = details.objects.all().select_related('emp_name').select_related('salary')
    
    print(abc)
    return render(request,'join.html',{'d':abc})










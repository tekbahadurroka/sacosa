from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Max
# Create your views here.


@login_required(login_url='/')
def HOME(request):
    return render(request,'admin/home.html')

@login_required(login_url='/')
def branch_add(request):
    code = 100 if BranchSetup.objects.count() == 0 else BranchSetup.objects.aggregate(max=Max('branch_code'))["max"]+1
    if request.method == 'POST':
        branch_name = request.POST.get('branch_name')
        branch_address = request.POST.get('branch_address')
        branch = BranchSetup(
            branch_code=code,
            branch_name = branch_name,
            address = branch_address,
            )
        branch.save()
        messages.success(request,'Successfully Branch Setup')
        return redirect('view_branch')
    return render(request,'admin/add_branch.html')

@login_required(login_url='/')
def branch_view(request):
    branch = BranchSetup.objects.all()
    context = {
        'branch':branch
    }
    return render(request,'admin/view_branch.html',context)

@login_required(login_url='/')
def branch_edit(request,id):
    data = BranchSetup.objects.get(id=id)
    if request.method == 'POST':
        data.branch_code = request.POST['branch_code']
        data.branch_name = request.POST['branch_name']
        data.address = request.POST['branch_address']
        
        data.save()
        messages.success(request,'Update Success')
        return redirect('view_branch')
    else:
        data = BranchSetup.objects.get(id=id)
           
    context = {
        'data':data
    }
    return render(request,'admin/edit_branch.html',context)
@login_required(login_url='/')
def delete_branch(request,id):
    delete = BranchSetup.objects.get(id=id)
    delete.delete()
    messages.success(request,'Successfully Deleted')
    return redirect('view_branch')

@login_required(login_url='/')
def register(request):
    branch = BranchSetup.objects.all()
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('Password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        branch = request.POST.get('branch')
        picture = request.FILES.get('user_photo')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,"This email Already used")
            return redirect('register')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,"This username Already used")
            return redirect('register')
        
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                profile_pic=picture,
                user_type=2                
            )
            user.set_password(password)
            user.save()
            
        branch_id = BranchSetup.objects.get(id=branch)
        staff = StaffUser(
            admin = user,
            gender = gender,
            address = address,
            branch_id = branch_id,            
        )
        staff.save()
        messages.success(request,user.first_name + " " + user.last_name + " " + 'Staff Successfully Save !')
        return redirect('staff_views')
    context = {
        'branch':branch
    }
    return render(request,'admin/register.html',context)

@login_required(login_url='/')
def staff_views(request):
    satff_view = StaffUser.objects.all()
    context = {
        'satff_view':satff_view
    }
    return render(request,'admin/staff_views.html',context)

@login_required(login_url='/')
def staff_edit(request,id):
    staff_edit = StaffUser.objects.filter(id = id)
    branch = BranchSetup.objects.all()
    context = {
        'branch':branch,
        'staff_edit':staff_edit,
    }
    return render(request,'admin/staff_edit.html',context)
    
@login_required(login_url='/')   
def update_staff(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('Password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        branch_id = request.POST.get('branch')
        user_photo = request.FILES.get('user_photo')
        
        user = CustomUser.objects.get(id = staff_id)
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.username=username
          
        if password !=None and password !="":
            user.set_password(password)
        if user_photo !=None and user_photo !="":
            user.profile_pic = user_photo
        
        user.save()
        
        staff = StaffUser.objects.get(admin = staff_id)
        staff.gender = gender
        staff.address = address 
        branch = BranchSetup.objects.get(id=branch_id)
        staff.branch_id = branch
     
        staff.save()
        messages.success(request,'Successfully Update')
        return redirect('staff_views')
    
    return render(request,'admin/staff_edit.html')

@login_required(login_url='/')
def delete_staff(request,admin):
    data = StaffUser.objects.get(id=admin)
    data.delete()
    messages.success(request,'Successfully Delete')
    return redirect('staff_views')
    

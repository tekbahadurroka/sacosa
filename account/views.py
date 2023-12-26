from django.shortcuts import render,redirect,HttpResponse
from .EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser


@login_required(login_url='/')
def base(request):
    return render(request,'base.html')

@login_required(login_url='/')
def LOGIN(request):
    return render(request,'index.html')

@login_required(login_url='/')
def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                        username=request.POST.get('username'),
                                        password=request.POST.get('password'),)
        if user!=None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('home') 
            elif user_type == '2':
               return HttpResponse('this page is HOD page')
            elif user_type == '3':
                return HttpResponse('this page is BM page')
            elif user_type == '4':
                return HttpResponse('this page is Staff page')
            else:
                messages.error(request,'Username and password are invalid !!')
                return redirect('login') 
        else:
            messages.error(request,'Username and password are invalid !!')
            return redirect('login')

def doLogout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id = request.user.id)
    
    context = {
        "user": user,
    }
    return render(request,'profile.html',context)

@login_required(login_url='/')
def profile_update(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        #email = request.POST.get('email')
        #useuname = request.POST.get('username')
        password = request.POST.get('password')
       
        try:
            customuser = CustomUser.objects.get(id = request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            
            if password !=None and password !="":
                customuser.set_password(password)
                
            if profile_pic !=None and profile_pic !="":
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request,"Profile Update Success")
            return redirect('profile')            
        except:
            messages.error(request,"Update Failed")       
    
    return render(request, 'profile.html')

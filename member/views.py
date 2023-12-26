import json
from django.core import serializers
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from adminstrator_app.models import BranchSetup,StaffUser
from account.models import CustomUser
from django.http import JsonResponse
from django.views import View
from .models import *

# Create your views here.
@login_required(login_url='/')
def center_setup(request):
    branche = BranchSetup.objects.all()
    if request.method == 'POST':
        branch = request.POST['branch']
        center_code = request.POST['center_code']
        center_name = request.POST['center_name']
        center_address = request.POST['center_address']
        meeting_day = request.POST['meeting_day']
        next_meeting = request.POST['next_meeting']
        branch_id = BranchSetup.objects.get(id=branch)
        center = CenterDetails(
            branch_id = branch_id,
            center_no = center_code,
            center_name = center_name,
            center_address = center_address,
            meeting_date = meeting_day,
            next_meeting_date = next_meeting,
        )
        center.save()
        messages.success(request,'Center Successfully Add')
        return redirect('view_center')
    context = {
        'branch':branche,
    }
    return render(request,'bm/center_setup.html',context)

@login_required(login_url='/')
def center_view(request):
    
    center_view = CenterDetails.objects.all()
    context = {
        'center_view':center_view,
    }
    
    return render(request,'bm/view_center.html',context)

def center_edit(request,id):
    branche = BranchSetup.objects.all()
    center = CenterDetails.objects.get(id = id)
    if request.method == 'POST':
        branch = request.POST['branch']
        center.center_no = request.POST['center_code']
        center.center_name = request.POST['center_name']
        center.center_address = request.POST['center_address']
        center.meeting_date = request.POST['meeting_day']
        center.next_meeting_date = request.POST['next_meeting']
        branch_id = BranchSetup.objects.get(id =branch)
        center.branch_id = branch_id
        center.save()
        messages.success(request,'Successfully Update')
        return redirect('view_center')
    else:
        center = CenterDetails.objects.get(id = id)
    context = {
        'branch':branche,
        'center':center,
    }   
    return render(request,'bm/edit_center.html',context)

@login_required(login_url='/')
def center_delete(request,id):
    center_delete = CenterDetails.objects.get(id = id)
    center_delete.delete()
    messages.success(request,'Successfuly Deleted')
    return redirect('view_center')

def group_setup(request):
    branch = BranchSetup.objects.all()
    if request.method == 'POST':
        branch_id = request.POST.get('branch')
        center = request.POST.get('center')
        group_code = request.POST.get('group_code')
        branch_id = BranchSetup.objects.get(id = branch_id)
        center_id = CenterDetails.objects.get(id = center)
        
        data = GroupCreate(
            branch_name = branch_id,
            center_no = center_id,
            group = group_code,
        )
        data.save()
        messages.success(request,'Group Successfuly created')
        return redirect('view_group')
    d = {'branch': branch}
    return render(request,'bm/group_add.html',d)

def load_center(request):
    branch_id = request.GET.get('branch')
    center = CenterDetails.objects.filter(branch_id=branch_id).order_by('center_no')
    return render(request, 'bm/get-center.html', {'center': center})



@login_required(login_url='/')
def group_view(request):
    group = GroupCreate.objects.all()
    context = {
        'group':group,
    }
    return render(request,'bm/view_group.html',context)


@login_required(login_url='/')
def member_entry(request):
    branch = BranchSetup.objects.all()
    if request.method == 'POST':
        branch_id = request.POST.get('branch')
        center = request.POST.get('center')
        group = request.POST.get('group')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        citizenship = request.POST.get('citizenship')
        issue_date = request.POST.get('issue_date')
        place = request.POST.get('place')
        religion = request.POST.get('religion')
        category = request.POST.get('category')
        district = request.POST.get('district')
        municipilaty = request.POST.get('municipilaty')
        worda = request.POST.get('worda')
        village = request.POST.get('village')
        father = request.POST.get('father')
        spouse = request.POST.get('spouse')
        spouse_dob = request.POST.get('spouse_dob')
        spouse_citizen = request.POST.get('spouse_citizen')
        spouse_issue = request.POST.get('spouse_issue')
        spouse_place = request.POST.get('spouse_place')
        soccupation = request.POST.get('soccupation')
        grandfather = request.POST.get('grandfather')
        tdistrict = request.POST.get('tdistrict')
        tmunicipilaty = request.POST.get('tmunicipilaty')
        tworda = request.POST.get('tworda')
        tvillage = request.POST.get('tvillage')
        member_photo = request.FILES.get('member_photo')
        citizen_copy = request.FILES.get('citizen_copy')
        sig_card = request.FILES.get('sig_card')
        branch_id = BranchSetup.objects.get(id = branch_id )
        center_no = CenterDetails.objects.get(id = center)
        group_no = GroupCreate.objects.get(id = group)
        member = MemberEntry(
            branch = branch_id,
            center = center_no,
            group = group_no,
            first_name = first_name,
            last_name = last_name,
            phone_number = mobile,
            email = email,
            gender = gender,
            date_of_birth = dob,
            citizenship_no = citizenship,
            issue_date = issue_date,
            issue_place = place,
            religion = religion,
            category = category,
            district = district,
            municipilaty = municipilaty,
            worda = worda,
            village = village,
            father = father,
            spouse = spouse,
            spouse_dob = spouse_dob,
            s_citizenship = spouse_citizen,
            s_issue_date = spouse_issue,
            s_place = spouse_place,
            s_occupation = soccupation,
            father_inlow = grandfather,
            tdistrict = tdistrict,
            tmunicipilaty = tmunicipilaty,
            tworda = tworda,
            tvillage = tvillage,
            photo = member_photo,
            citizenship_copy = citizen_copy,
            signature_card = sig_card,
        )
        member.save()
        messages.success(request,'Successfully Submited Data')
        return redirect('member_view')
    d = {'branch': branch}
    return render(request,'bm/member_entry.html',d)

def load_group(request):
    center_id = request.GET.get('center')
    group = GroupCreate.objects.filter(center_no=center_id).order_by('group')
    return render(request, 'bm/get_group.html', {'group': group})

def member_views(request):
    member_view = MemberEntry.objects.all()
    context = {
        'member_view':member_view,
    }
    return render(request,'bm/member_views.html',context)
def member_edit(request,id):
    branch = BranchSetup.objects.all()
    member = MemberEntry.objects.filter(id=id)
    
    context = {
        'branch':branch,
        'member':member,
    }
    return render(request,'bm/member_edit.html',context)

def member_update(request):
    if request.method == 'POST':
        member_id = request.POST.get('member_id')
        branch_id = request.POST.get('branch')
        center = request.POST.get('center')
        group = request.POST.get('group')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        citizenship = request.POST.get('citizenship')
        issue_date = request.POST.get('issue_date')
        place = request.POST.get('place')
        religion = request.POST.get('religion')
        category = request.POST.get('category')
        district = request.POST.get('district')
        municipilaty = request.POST.get('municipilaty')
        worda = request.POST.get('worda')
        village = request.POST.get('village')
        father = request.POST.get('father')
        spouse = request.POST.get('spouse')
        spouse_dob = request.POST.get('spouse_dob')
        spouse_citizen = request.POST.get('spouse_citizen')
        spouse_issue = request.POST.get('spouse_issue')
        spouse_place = request.POST.get('spouse_place')
        soccupation = request.POST.get('soccupation')
        grandfather = request.POST.get('grandfather')
        tdistrict = request.POST.get('tdistrict')
        tmunicipilaty = request.POST.get('tmunicipilaty')
        tworda = request.POST.get('tworda')
        tvillage = request.POST.get('tvillage')
        member_photo = request.FILES.get('member_photo')
        citizen_copy = request.FILES.get('citizen_copy')
        sig_card = request.FILES.get('sig_card')
       
        
        member = MemberEntry.objects.get(id = member_id)
        member.first_name = first_name
        member.last_name = last_name
        member.phone_number = mobile
        member.email = email
        member.gender = gender
        member.date_of_birth = dob
        member.citizenship_no = citizenship
        member.issue_date = issue_date
        member.issue_place = place
        member.religion = religion
        member.category = category
        member.district = district
        member.municipilaty = municipilaty
        member.worda = worda
        member.village = village
        member.father = father
        member.spouse = spouse
        member.spouse_dob = spouse_dob
        member.s_citizenship = spouse_citizen
        member.s_issue_date = spouse_issue
        member.s_place = spouse_place
        member.s_occupation = soccupation
        member.father_inlow = grandfather
        member.tdistrict = tdistrict
        member.tmunicipilaty = tmunicipilaty
        member.tworda = tworda
        member.tvillage = tvillage
        if member_photo !=None and member_photo !="":
            member.photo = member_photo
            
        if citizen_copy !=None and citizen_copy !="":
            member.citizenship_copy = citizen_copy
            
        if sig_card !=None and sig_card !="":
            member.signature_card = sig_card
        
        branch_id = BranchSetup.objects.get(id = branch_id )
        member.branch = branch_id
        center_no = CenterDetails.objects.get(id = center)
        member.center = center_no
        group_no = GroupCreate.objects.get(id = group)
        member.group = group_no
            
            # photo = member_photo,
            # citizenship_copy = citizen_copy,
            # signature_card = sig_card,

        member.save()
        messages.success(request,'Successfully Updated Data')
        return redirect('member_view')
    
    return render(request,'bm/member_edit.html')

def member_delete(request,id):
    member_delete = MemberEntry.objects.get(id=id)
    member_delete.delete()
    messages.success(request,'Successfuly Member Deleted')
    return redirect('member_view')

def kyc_view(request,id):
    branch = BranchSetup.objects.all()
    member = MemberEntry.objects.filter(id=id)
    
    context = {
        'branch':branch,
        'member':member,
    }
    
    return render(request,'bm/kyc_views.html',context)

def search_box(request):
    search = MemberEntry.objects.all()
    #branches = BranchSetup.objects.all()
    context = {
        'search':search,
        #'branches':branches
    }
    return render(request,'bm/search_box.html',context)

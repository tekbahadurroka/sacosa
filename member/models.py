from django.db import models
from account.models import CustomUser
from adminstrator_app.models import BranchSetup,StaffUser
import datetime
from django.utils import timezone

# # Create your models here.
class CenterDetails(models.Model):
    branch_id = models.ForeignKey(BranchSetup,on_delete=models.CASCADE)
    center_no = models.CharField(max_length=3)
    center_name = models.CharField(max_length=350)
    center_address = models.CharField(max_length=550)
    meeting_date = models.CharField(max_length=100)
    next_meeting_date = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.center_no + " " + self.center_name + " "+ self.branch_id.branch_name
       
class GroupCreate(models.Model):
    branch_name = models.ForeignKey(BranchSetup,on_delete=models.DO_NOTHING)
    center_no = models.ForeignKey(CenterDetails,on_delete=models.CASCADE)
    group =models.CharField(max_length=5, blank=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.group

class MemberEntry(models.Model):
    branch = models.ForeignKey(BranchSetup,on_delete=models.CASCADE)
    center = models.ForeignKey(CenterDetails,on_delete=models.CASCADE)
    group = models.ForeignKey(GroupCreate,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=150)
    gender = models.CharField(max_length=15)
    date_of_birth = models.CharField(max_length=150)
    citizenship_no = models.CharField(max_length=150)
    issue_date = models.CharField(max_length=150)
    issue_place = models.CharField(max_length=200)
    religion = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    district = models.CharField(max_length=150)
    municipilaty = models.CharField(max_length=150)
    worda = models.IntegerField(default=0)
    village = models.CharField(max_length=150)
    father = models.CharField(max_length=150)
    spouse = models.CharField(max_length=150)
    spouse_dob = models.CharField(max_length=150)
    s_citizenship = models.CharField(max_length=150)
    s_issue_date = models.CharField(max_length=150)
    s_place = models.CharField(max_length=150)
    s_occupation = models.CharField(max_length=350)
    father_inlow = models.CharField(max_length=150)
    tdistrict = models.CharField(max_length=150)
    tmunicipilaty = models.CharField(max_length=150)
    tworda = models.IntegerField(default=0)
    tvillage = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='media/images')
    citizenship_copy = models.ImageField(upload_to='media/images')
    signature_card = models.ImageField(upload_to='media/images')
    
    def __str__(self):
        return self.first_name +" "+ self.last_name
    

                            
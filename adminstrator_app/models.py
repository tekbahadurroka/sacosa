from django.db import models
from account.models import CustomUser
import uuid

# Create your models here.
class BranchSetup(models.Model):
    branch_code = models.IntegerField(default=uuid.uuid4, editable=False, unique=True)
    branch_name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.branch_name

class StaffUser(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    address = models.TextField()
    branch_id = models.ForeignKey(BranchSetup,on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True,null=True)
    update_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.admin.first_name +" " + self.admin.last_name
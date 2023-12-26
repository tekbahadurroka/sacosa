from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(BranchSetup)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['id','branch_code','branch_name','address','create_date','update_date']

admin.site.register(StaffUser)


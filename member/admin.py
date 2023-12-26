from django.contrib import admin
from .models import *

#admin.site.register(CenterDetails)
@admin.register(CenterDetails)
class CenterAdmin(admin.ModelAdmin):
    list_display = ['id','branch_id','center_no','center_name','center_address','meeting_date','next_meeting_date','create_date','update_date']

@admin.register(GroupCreate)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id','branch_name','center_no','group','create_at','update_at']
    
admin.site.register(MemberEntry)

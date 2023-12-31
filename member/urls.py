
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views


urlpatterns = [
    path('add_center', views.center_setup, name="add_center"),
    path('view_center', views.center_view, name="view_center"),
    path('edit_center/<str:id>', views.center_edit, name="edit_center"),
    path('delete_center/<str:id>', views.center_delete, name="delete_center"),
    path('add_group', views.group_setup, name="add_group"),
    path('load_center', views.load_center, name="ajax_load_center"),
    path('view_group', views.group_view, name="view_group"),
    path('member_entry', views.member_entry, name="member_entry"),
    path('load_group', views.load_group, name="ajax_load_group"),
    path('member_view', views.member_views, name="member_view"),
    path('member_edit/<str:id>', views.member_edit, name="member_edit"),
    path('member_update', views.member_update, name="member_update"),
    path('member_delete/<str:id>', views.member_delete, name="member_delete"),
    path('kyc_view/<str:id>', views.kyc_view, name="kyc_view"),
    path('search_box', views.search_box, name="search_box"),
    path('branch_see', views.branch_see, name="branch_see"),
   
      
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
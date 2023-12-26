
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views


urlpatterns = [
    path('home', views.HOME, name="home"),
    path('register', views.register, name="register"),
    path('staff_views', views.staff_views, name="staff_views"),
    path('staff_edit/<str:id>', views.staff_edit, name="staff_edit"),
    path('update', views.update_staff, name="update_staff"),
    path('delete_staff/<str:admin>', views.delete_staff, name="delete_staff"),
    path('branch_add', views.branch_add, name="add_branch"),
    path('branch_view', views.branch_view, name="view_branch"),
    path('branch_edit/<str:id>', views.branch_edit, name="edit_branch"),
    path('branch_delete/<str:id>', views.delete_branch, name="delete_branch"),
    

    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
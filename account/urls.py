from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('base',views.base,name="base"),
    # path('login', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='Logout'),
    path('profile', views.PROFILE, name='profile'),
    path('profile/update', views.profile_update, name='profile_update'),
    
   
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
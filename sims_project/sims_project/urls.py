from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import TemplateView 
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls), 
    path('account/', include('account.urls')), 
    path('101/', include('sims101.urls')),    
    path('102/', include('sims102.urls')),   

]

from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import TemplateView 

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'), 
    path('admin/', admin.site.urls),
    path('101/', include('sims101.urls')),   # include 에는 name을 부여할 수 없다 
    path('102/', include('sims102.urls')),   # include 에는 name을 부여할 수 없다 
]

# app_name = 'account'  domain  in urls.py 
# You need to use that namespace when reversing urls with reverse/reverse_lazy or {% url %}:
#  for example,  LOGIN_REDIRECT_URL = reverse_lazy('account:dashboard')
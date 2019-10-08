from django.urls import path
from . import views

app_name = 'sims101'

urlpatterns = [ 
    path('', views.IndexListView.as_view(), name='index_list'), 
    path('data/<int:pk>/', views.IndexDetailView.as_view(), name='index_detail'), 
    path('data/create/', views.IndexCreateView.as_view(), name='index_create'), 
    path('data/<int:pk>/update', views.IndexUpdateView.as_view(), name='index_update'),
    path('data/<int:pk>/delete', views.IndexDeleteView.as_view(), name='index_delete'), 

]


# app_name = 'account'  domain  in urls.py 
# You need to use that namespace when reversing urls with reverse/reverse_lazy or {% url %}:
#  for example,  LOGIN_REDIRECT_URL = reverse_lazy('account:dashboard')
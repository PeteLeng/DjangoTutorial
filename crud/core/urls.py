from django.urls import path
from . import views

urlpatterns = [
    path('', views.emp_list, name='emp-list'),
    path('create/', views.emp_create, name='emp-create'),
    path(r'^edit/(?P<pk>\d+)/$', views.emp_edit, name='emp-edit'),
    path('delete/', views.emp_delete, name='emp-delete'),
]

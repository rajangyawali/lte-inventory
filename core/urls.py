from django.urls import path, re_path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('edit/<str:site_id>/', views.siteEdit, name='site-edit'),
    path('detail/<str:site_id>/', views.siteDetail, name='site-detail'),
    path('delete/<str:site_id>/', views.siteDelete, name = 'site-delete'),
    path('create/', views.siteCreate, name='site-create'),
    path('employees', views.employeeInfo, name='employees'),
    path('owners/', views.ownerInfo, name='owners'),
    path('update/', views.editProfile, name='editProfile'),
    path('employee-create/', views.employeeCreate, name='employee-create'),
    path('employee-edit/<employee_id>/', views.employeeEdit, name='employee-edit'),
    path('employee-delete/<employee_id>/', views.employeeDelete, name='employee-delete'),
    path('owner-edit/<id>/', views.ownerEdit, name='owner-edit'),
    path('changepw/', views.changePassword, name = 'changePassword'),
]
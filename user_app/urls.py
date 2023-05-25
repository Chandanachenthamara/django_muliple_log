# from django.urls import path
# from .views import *
# urlpatterns = [
#     path('', index,name='index'),
#     path('customer', CustomerSignUpView.as_view(), name='customer_signup'),
#     path('manager', ManagerSignUpView.as_view(), name='manager_signup'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('employee/', views.employee, name='employee'),
]

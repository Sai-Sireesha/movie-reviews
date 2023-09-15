from django.urls import path
from . import views

urlpatterns = [
    path('account_signup/', views.account_signup, name='account_signup'),
    path('logout/', views.account_logout, name='account_logout'),
    path('login/', views.account_login, name='account_login'),
]
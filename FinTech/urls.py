
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard',views.dashboard,name="dashboard"),
    path('income',views.income,name="income"),



    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
]

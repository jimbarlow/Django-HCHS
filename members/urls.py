from django.urls import path
from . import views

urlpatterns = [

   # path('register/', UserRegisterView.asview(), name='register'),
   path('login_user/', views.login_user, name='login' ),
   path('logout_user/', views.logout_user, name='logout'),
]

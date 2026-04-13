from django.urls import path
from . import views

app_name =  'users'

urlpatterns = [
  path('login/', views.LoginView.as_view(), name='login'),
  path('signup/', views.SignupView.as_view(), name='Signup'),
  path('profile/', views.ProfileView.as_view(), name='profile'),
  path('logout/', auth_views.LogoutView.as_view(next_page='users:login'), name='logout'),
  

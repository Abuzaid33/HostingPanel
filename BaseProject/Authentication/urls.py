from django.urls import path
from Authentication import views
urlpatterns = [
  
    path('signup/', views.signuppage, name='signup'),
    path('', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),

]
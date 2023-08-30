from django.contrib import admin
from django.urls import path
from Baseapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signuppage, name='signup'),
    path('login/', views.loginpage, name='login'),
    path('home/', views.home_view, name='home'),  # Update the view function name
    path('logout/', views.logoutpage, name='logout'),
]

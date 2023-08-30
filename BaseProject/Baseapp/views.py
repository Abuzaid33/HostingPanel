from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def home_view(request):
    return render(request, 'home.html')

def signuppage(request):
    if request.method == 'POST':
        username = request.POST.get('fullname')  # Update to 'fullname' from 'username'
        email = request.POST.get('emailaddress')  # Update to 'emailaddress' from 'email'
        password = request.POST.get('password')  # Update to 'password' from 'password1'
        confirm_password = request.POST.get('password-confirm')  # New field for password confirmation

        if password != confirm_password:
            return HttpResponse("Your passwords do not match")
        else:
            # Create a new user
            my_user = User.objects.create_user(username, email, password)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')
    
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to 'home' page upon successful login
        else:
            return HttpResponse("Invalid credentials")

    return render(request, 'login.html')


def logoutpage(request):
    logout(request)  # Logs out the user
    return render(req
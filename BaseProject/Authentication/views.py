from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm




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
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Store user information in the session
            request.session['user_id'] = user.id
            request.session['user_username'] = user.username
            request.session['user_full_name'] = user.get_full_name()  # Customize this based on your user model

            # Redirect to the home page or any other desired page
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logoutpage(request):
    # Log the user out and clear the session
    logout(request)
    return redirect('logout')
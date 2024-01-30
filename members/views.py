from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# class UserRegisterView(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('login')

def login_user(request):
    # return render(request, 'authenticate/registration/login.html', {})
    print ("got to the login_user view")
    if request.method == "POST":
        print ("the request.method was POST")
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print ( user.username )
            login(request, user)
            # loggin_user = request.session['username']
            # login_user = username
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            print ("failed login")
            messages.success(request, "There was an error logging in, try again.")
            return redirect('login')
    else:
        print ("request method was not POST")
        return render(request, 'registration/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You Were Successfully Logged Out")
    return redirect('home')
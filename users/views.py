from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def login(request):
    return render(request, 'users/login.html')

def signup(request):
    if request.method == "POST":
       
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request,"Your Account has been successfully created.")

        return redirect('signin')

    return render(request,"register/signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username)
        passw = authenticate(password=pass1)

        if user is not None:
            login(request,user,passw)
            fname = user.first_name
            return redirect('home')

        else:
            messages.error(request,"Bad Credentials")
            return redirect('home')    

    return render(request,"register/signin.html")


def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect('')


@login_required
def account(request):
    context = {
        'account_page': "active",
    }
    return render(request, 'users/account.html', context)
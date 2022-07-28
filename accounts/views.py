from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from . import forms as auth_forms

# Create your views here.
@require_http_methods(["GET"])
def index(request):
    return render(request, "accounts/index.html")

@require_http_methods(["GET", "POST"])
def register(request): # Registration View
    if request.method == "POST":
        reg_form = auth_forms.UserRegForm(request.POST)

        if reg_form.is_valid():
            first_name = reg_form.cleaned_data["first_name"]
            last_name = reg_form.cleaned_data["last_name"]
            username = reg_form.cleaned_data["username"]
            email = reg_form.cleaned_data["email"]
            password1 = reg_form.cleaned_data["password1"]
            password2 = reg_form.cleaned_data["password2"]

            if User.objects.filter(email=email).exists():
                print('Email already exists!')
                return redirect("accounts:register")
            
            elif User.objects.filter(username=username).exists():
                print("Username already exists!")
                return redirect("accounts:register")
            
            elif password1 != password2:
                print("Passwords don't match!")
                return redirect("accounts:register")
            
            else:
                new_user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password1
                )
                new_user.save()
                print("New user created!")
                return redirect("accounts:login")
        else:
            print("Invalid form!")
            return redirect("accounts:register")

    else:
        reg_form = auth_forms.UserRegForm()
        context = {
            "reg_form": reg_form
        }
        return render(request, "accounts/register.html", context)

@require_http_methods(["GET", "POST"])
def login(request): # Login View
    if request.method == "POST":
        user_form = auth_forms.LoginForm(request.POST)

        if user_form.is_valid():
            username = user_forms.cleaned_data["username"]
            password = user_forms.cleaned_data["password"]
            
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                print("User logged in!")
                return redirect("notesapp:index")
            
            else:
                print("Invalid credentials")
                return redirect("accounts:login")

        else:
            print("Invalid form!")
            return redirect("accounts:login")
    
    else:
        login_form = auth_forms.LoginForm()
        context = {
            "login_form": login_form
        }
        return render(request, "accounts/login.html", context)

@require_http_methods(["GET"])
@login_required
def logout(request): # Logout View
    user = request.user
    auth.logout(user)
    print("User logged out!")
    return render(request, "notesapp:index")
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from . import forms
from .forms import LoginForm,RegisterForm


# Create your views here.
def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {'form':login_form}

    if login_form.is_valid():
        username= login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
    return render(request,"accounts/login.html",context)


User = get_user_model()

def register_page(request):
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        username = register_form.cleaned_data.get("username")
        password = register_form.cleaned_data.get("password")
        email = register_form.cleaned_data.get("email")
        new_user = User.objects.create_user(username, email, password)
    return render(request,"accounts/register.html",{"form":register_form})


def home_page(request):
    context = {
        'title':'Hello world',
        'content':'Welcome to the home page'
    }
    return render(request,'home_page.html',context)

def contact_page(request):
    contact_form = forms.Contact_Form(request.POST or None)
    context = {
        "title":"Contact page",
        "content":"Welcome to the contact page",
        "form":contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method=="POST":
    #     print(request.POST.get("name"))
    #     # if contact_form.is_valid():
    #     #     print(contact_form.cleaned_data)

    return render(request,'contact/view.html',context)

def logout_page(request):
    if request.user is not None:
        logout(request)
        return redirect("/")
    # return render(request, "auth/logout.html", {})


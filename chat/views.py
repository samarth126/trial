from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, forms, login, logout
from django.http import HttpResponse
from chat.forms import UserRegistrationForm , UserLoginForm
# Create your views here.



def index(request):
    return render(request, 'index.html')



def dashboard(request):
    return render(request, 'dashboard.html')


def register(request):
    context={}
    if request.POST:
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context['register_form']=form

    else:
        form=UserRegistrationForm()
        context['register_form']=form
    return render(request, "register.html", context)


def login_view(request):
    context={}
    if request.POST:
        form=UserLoginForm(request.POST) 
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect("dashboard")
        else:     
            context['login_form']=form
    else:
        form=UserLoginForm()
        context["login_form"]=form
    return render(request, "login.html", context)



def logout_view(request):
    logout(request)
    return redirect('login')




        
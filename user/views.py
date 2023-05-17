from django.shortcuts import render,redirect
from .form import Kayıtol,Login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout#modüller önemli!!!
from django.views.decorators.csrf import csrf_protect
# Create your views here.
@csrf_protect
def login1(request):
    form=Login(request.POST or None)
    content={
        "form":form#2side form olması lazım
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Kullanıcı Adınız veya Şifreniz Yanlış !")
            return render(request,"login.html",content)
        login(request,user)
        messages.success(request,"Başarıyla Giriş Yaptınız !")
        return redirect("index")
    return render(request,"login.html",content)

def register(request):
    form=Kayıtol(request.POST or None)
    if form.is_valid():#eğer parolarımız eşleşmeyi sağlarsa ve parantez önemli !!!
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        newuser=User(username = username)
        newuser.set_password(password)
        newuser.save()
        login(request,newuser)
        messages.success(request,"Başarıyla Kayıt Oldunuz !")
        return redirect("index")
    content={
        "form":form#2side form olması lazım
    }
    return render(request,"register.html",content)
def logout1(request):
    logout(request)
    messages.success(request,"Çıkış Yaptınız !")
    
    return redirect("index")
from django.shortcuts import render,redirect
from service.models import gym
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/register/')
def home(request):
    context={}
    if request.method =="POST":
        n=request.POST.get('name')
        cont=request.POST.get('contact')
        gen=request.POST.get('gender')
        add=request.POST.get('address')

        gym.objects.create(name=n,contact=cont,gender=gen,address=add)
        queryset=gym.objects.all()
        context["home"]=queryset

    
    queryset=gym.objects.all()
    context["home"]=queryset
    return render(request,'base.html',context)


def delete(request,id):
     queryset=gym.objects.get(id=id)
     queryset.delete()
     return redirect('/home')

def update(request,id):
     queryset=gym.objects.get(id=id)
     if request.method=="POST":
        n=request.POST.get('name')
        cont=request.POST.get('contact')
        gen=request.POST.get('gender')
        add=request.POST.get('address')
            
        queryset.name=n
        queryset.contact=cont
        queryset.gender=gen
        queryset.address=add
        
        queryset.save()
        return redirect('/home')
     context={'upp':queryset}
     return render(request,"update.html",context)



def log(request):

    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        if not User.objects.filter(username =  username).exists():
            messages.error(request, 'invalid usrename')
            return redirect('/log')
        
        user = authenticate(username = username , password = password)

        if user is None:
            messages.error(request, 'invalid password')
            return redirect('/log')
        else:
            login(request, user)
            return redirect('/home')
        
        
    return render(request,'log.html')

def logo(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method=="POST":
        firstname=request.POST.get("first_name")
        lastname=request.POST.get("last_name")
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=User.objects.filter(username= username)
        if user.exists():
            messages.info(request,"username already exist")
            return redirect('/register')
        
        user=User.objects.create(first_name=firstname,last_name=lastname,username=username)
        user.set_password(password)
        user.save()
        messages.info(request,"account created")
        return redirect('/register')
    return render(request,'register.html')



def test(request):
    return render(request,'test.html')

    
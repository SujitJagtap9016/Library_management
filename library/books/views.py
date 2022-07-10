from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from django.views.generic import UpdateView
# Create your views here.
def home(request):
    return render(request,'home.html')

def loginuser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user_obj = CustomUser.objects.filter(email = email).first()
        if user_obj is None:
            messages.success(request, ("User is not registered"))
            print("no user")
            return redirect('loginuser')
              
        user = authenticate(email = email , password = password)
        if user is None:
            messages.success(request, ("Login failed"))
            print("no")
            return redirect('loginuser')

        login(request, user)
        if user.is_staff:
            return redirect('adminprofile')
        else:
            return redirect('studentprofile')
        
        
    return render(request,'loginuser.html')

def logoutuser(request):
    logout(request)
    return redirect("home")

def registeruser(request):
    if request.method=="POST":
        fname = request.POST["first"]
        last = request.POST["last"]
        
        pwd = request.POST["password"]
        em = request.POST["email"]
        con = request.POST["phone"]
        tp = request.POST["utype"]
        try:
            CustomUser.objects.get(email= em)
            messages.success(request, ("Email already registered"))
            print("Email already registered")
        except CustomUser.DoesNotExist:
            usr = CustomUser.objects.create_user(em,pwd)
            usr.first_name = fname
            usr.last_name = last
            if tp=="admin":
                usr.is_staff = True
                usr.save()

            reg = register(user=usr, phone=con,user_type=tp)
            reg.save()
            messages.success(request, ("User Registered Successfully"))
    return render(request,'registeruser.html')


def studentprofile(request):

    book = books.objects.all()
    
    return render(request,"studentprofile.html",{
         'book':book,
         
    }) 

def adminprofile(request):
    return render(request,'adminprofile.html')

def addbook(request):
    if request.method == "POST":
        id = request.POST.get('id')
        name = request.POST.get('name')
        author = request.POST.get('author')
        publisher = request.POST.get('publisher')
        book=books(id=id,name=name,author=author,publisher=publisher)
        book.save()
        return redirect('viewbook')
    else:
        return render(request,'addbook.html')

def updatebook(request,id):
   book=books.objects.get(pk=id)
   
   return render(request,'updatebook.html',{'book':book})


def deletebook(request,id):
    book=books.objects.get(id=id)
    book.delete()
    return redirect('viewbook')
def viewbook(request):
    book = books.objects.all()
    
    return render(request,"viewbook.html",{
         'book':book
    }) 



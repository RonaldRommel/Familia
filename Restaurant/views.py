from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu,Book
# Create your views here.
def home(request):
    return render(request,"index.html",{"confirm":None})

def about(request):
    return render(request,"about.html",{})

def menu(request):
    items=Menu.objects.all().order_by('name')
    return render(request,"menu.html",{"menu":items})

def menu_item(request,pk=None):
    if pk:
        try:
            item=Menu.objects.get(pk=pk)
        except:
            item=''
    else:
        item=''
    return render(request,"menu_item.html",{"menu_item":item})

def book(request):
    if request.method == "POST":
        name=request.POST.get("name","")
        email=request.POST.get("email","")
        phone=request.POST.get("phone","")
        requests=request.POST.get("requests","")
        guests=request.POST.get("guests",0)
        data=Book(name=name,email=email,phone=phone,requests=requests,guests=guests)
        data.save()
        print(name,email,phone)
        return render(request,"index.html",{})
    else:
        return render(request,"book.html",{})
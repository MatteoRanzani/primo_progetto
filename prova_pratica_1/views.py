from django.shortcuts import render
import random

# Create your views here.

def index(request):
    return render(request,"index.html")

def maxmin(request):
    var1=random.randint(1,10)
    var2=random.randint(1,10)
    var3=var1+var2
    context={
        'var1': var1,
        'var2': var2,
        'var3': var3,
    }
    return render(request, "maxmin.html", context)

def media(request): 
    num = []
    cont=0
    for i in range (30): 
        n=random.randint(1,10)
        num.append(n)
        cont+=n
    media=cont/30

    context = {
        'lista' : num,
        'media' : media,
    }
    return render(request,"media.html", context)

   

def voti(request):
    return render(request,"voti.html")

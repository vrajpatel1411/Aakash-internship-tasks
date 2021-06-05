from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vraj(request):
    return HttpResponse("Hello myself vraj")

def home(request):
    return render(request,"home.html")

def about(request):
    if request.method=="POST":
        print(request.POST)
        a=request.POST['na']
        return render(request,"about.html",{'sum':a})
    

def contact(request):
    if request.method=="POST":
        print(request.POST)
        a=int(request.POST['n'])
        b=int(request.POST['no'])
        c=a+b
        return render(request,"about.html",{'sum':c})
    
    
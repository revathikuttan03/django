from django.shortcuts import render,redirect
from django.http import HttpResponse

from myapp.models import TaskList
# Create your views here.


def home(request):
    data = TaskList.objects.all()
    return render(request,"home.html",{"dts":data})


def create(request):
    if request.GET.get("name"):
        nam = request.GET.get("name")
        description = request.GET.get("description")
        task = TaskList()
        task.name = nam
        task.description = description
        task.save()
        return redirect("/")
    return render(request,"create.html")



def update(request,tid):
    data = TaskList.objects.get(id=tid)
    if request.GET.get("name"):
       name = request.GET.get("name")
       description = request.GET.get("description")
       status = request.GET.get("status")
       print(name)
    
    return render(request,'update.html',{'d':data})
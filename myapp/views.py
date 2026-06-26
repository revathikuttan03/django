from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import TaskList
# Create your views here.


def home(request):
    data = TaskList.objects.all()
    return render(request,"home.html",{"datas":data})


def create(request):
    if request.GET.get("name"):
        name = request.GET.get("name")
        description = request.GET.get("description")
        print("fffffffffffffffffffffhttjjgjjjjjjjjjjjjjjjj\n",name,description)
    return render(request,"create.html")

from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import TaskList
# Create your views here.


def home(request):
    data = TaskList.objects.all()
    return render(request,"home.html",{"datas":data})
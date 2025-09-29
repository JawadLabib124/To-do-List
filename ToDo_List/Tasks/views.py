from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from Tasks import models
# Create your views here.


def home(req):
    tasks=models.Tasks
    task=tasks.objects.all()


    return render(req,'index.html',context={'task':task})

def addtask(req):
    database=models.Tasks
    if req.method=='POST':
        newtask=req.POST.get('title')
        description=req.POST.get('description')

        database.objects.create(NewTask=newtask,Description=description)
        return redirect('Tasks:home')
    
    return render(req,'index.html',context={})

        


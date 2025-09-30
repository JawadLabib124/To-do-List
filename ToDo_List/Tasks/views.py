from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from Tasks import models
# Create your views here.


def home(req):
    tasks=models.Tasks
    task=tasks.objects.order_by('-id')

    return render(req,'index.html',context={'task':task})

def addtask(req):
    database=models.Tasks
    if req.method=='POST':
        newtask=req.POST.get('title')
        description=req.POST.get('description')

        database.objects.create(NewTask=newtask,Description=description,completed='NO')
        return redirect('Tasks:home')
    
    return render(req,'index.html',context={})


def taskComplete(req,id):
    database=models.Tasks
    if req.method=="POST":
        task=database.objects.get(pk=id)
        task.completed='YES'
        task.save()
        return redirect('Tasks:home')
    
    return render(req,'index.html',context={})


def deleteTask(req,id):
    task=models.Tasks
    
    if req.method=="POST" or req.method=="GET":
        task=task.objects.get(pk=id)
        task.delete()
        return redirect('Tasks:home')
    return render(req,'index.html',context={})


def editTask(req,id):
    task=models.Tasks.objects.get(pk=id)
    if req.method=="POST":
        task.NewTask=req.POST.get('title')
        task.Description=req.POST.get('description')
        task.save()
        return redirect('Tasks:home')
    return render(req,'edit.html',context={'uid':id,'title':task.NewTask,'description':task.Description})
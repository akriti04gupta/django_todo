from django.shortcuts import render,redirect
from django.utils import timezone
from django.urls import reverse
from .models import Task

def task_list(request):
    tasks=Task.objects.all().order_by('-created_at')
    query = request.GET.get('query', '')
    created_date=request.GET.get('created_date','')
    start_date=request.GET.get('start_date','')
    end_date=request.GET.get('end_date','')
    if created_date:
        tasks = tasks.filter(created_at__date=created_date)
    if start_date:
        tasks = tasks.filter(start_date=start_date)
    if end_date:
        tasks = tasks.filter(end_date=end_date)
    if query:
        tasks = tasks.filter(title__icontains=query) | tasks.filter(id__icontains=query)
    return render(request,'task/task_list.html',{'tasks':tasks, 'query':query})

def task_add(request):
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        start_date=request.POST.get('start_date')
        end_date=request.POST.get('end_date')
        priority=request.POST.get('priority')
        if title:
            Task.objects.create(title=title,description=description,start_date=start_date,end_date=end_date,priority=priority)
            return redirect(reverse('task:task_list'))
    return render(request,'task/task_add.html')
    
def task_edit(request,id):
    task=Task.objects.get(id=id)
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        start_date=request.POST.get('start_date')
        end_date=request.POST.get('end_date')
        priority=request.POST.get('priority')
        if title:
            task.title=title
            task.description=description
            task.start_date=start_date
            task.end_date=end_date
            task.priority=priority
            task.save()
            return redirect(reverse('task:task_list'))
    return render(request,'task/task_update.html',{'task': task})

def task_delete(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('task:task_list')

def task_priority(request):
    task=Task.objects.all()
    priority=request.GET.get('priority','')
    if priority:
        task=task.filter(priority=priority)
    return render(request,'task/priority_list.html',{'task':task})

def task_toggle(request,id):
    task=Task.objects.get(id=id)
    if request.method =='POST':
        task.completed= not task.completed
        task.save()
    return redirect('task:task_list')

def task_status(request):
    task=Task.objects.all()
    status=request.GET.get('status','')
    if status == 'completed':
        task = task.filter(completed=True)
    if status == 'overdue':
        task = task.filter(completed=False,end_date__lt=timezone.now().date())
    return render(request, 'task/task_list.html', {'tasks': task})
    
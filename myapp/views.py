# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
# Create your views here.
def index(request):
    title = 'Welcome Django Course !!'
    return render(request,'index.html', {
        'title': title
    })

def about(request):
    username = 'Giovedy'
    return render(request,'about.html',{
        'username': username
    })    

def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)

def project(request):
    #project = list(Project.objects.values())
    #return JsonResponse(project, safe=False)
    project = Project.objects.all()
    return render (request,'project.html',{
        'project': project
    })

def task(request):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404 (Task, id=id)
    # return HttpResponse('task %s' % task.title)
    task = Task.objects.all()
    return render(request,'task.html', {
        'task': task
    })
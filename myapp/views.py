from turtle import title
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

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
    return render (request,'project/project.html',{
        'project': project
    })

def task(request):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404 (Task, id=id)
    # return HttpResponse('task %s' % task.title)
    task = Task.objects.all()
    return render(request,'task/task.html', {
        'task': task
    })

def create_task(request):
    # METHOD POST #
    if request.method == 'GET':
        return render(request,'task/create_task.html',{
        'forms': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('task')

    # METHOD GET #
    #print(request.GET)
    #print(request.GET['title'])
    #print(request.GET['description'])
    #Task.objects.create(title=request.GET['title'], description=request.GET['description'], project_id=2)
    #return render(request,'create_task.html',{
    #    'forms': CreateNewTask()
    #    })
def create_project(request):
    if request.method == 'GET':
        return render(request,'project/create_project.html',{
        'forms': CreateNewProject
    })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('project')

def project_detail(request, id):
    # project = Project.objects.get(id=id)
    project = get_object_or_404(Project, id=id)
    task = Task.objects.filter(project_id=id)
    print(project)
    return render(request,'project/project_detail.html',{
        'project': project,
        'task': task
    })


    
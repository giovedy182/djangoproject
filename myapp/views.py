from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    return HttpResponse("Index Page")

def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)

#def hello(request, id):
    #print(type(id))
    #result=id + 100 * 2
    #return HttpResponse("<h2>Hello %s</h2>" % result)

def about(request):
    return HttpResponse('about')

def project(request):
    project = list(Project.objects.values())
    return JsonResponse(project, safe=False)

def task(request, id):
    # task = Task.objects.get(id=id)
    task = get_object_or_404 (Task, id=id)
    return HttpResponse('task %s' % task.title)
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    #path('hello/<int:id>', views.hello),
    path('hello/<str:username>', views.hello),
    path('project/', views.project),
    #path('task/<int:id>', views.task)
    path('task/', views.task),
    path('create_task/', views.create_task)
]


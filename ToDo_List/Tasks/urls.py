from django.urls import path
from . import views
app_name='Tasks'
urlpatterns = [
    path('',views.home,name='home'),
    path('addTask/',views.addtask,name='addTask'),
    path('complete/<int:id>/',views.taskComplete,name='taskComplete'),
    path('delete/<int:id>/',views.deleteTask,name="DeleteTask"),
]
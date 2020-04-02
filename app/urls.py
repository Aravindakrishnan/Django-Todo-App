from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r"^$",views.index,name="index"),
    url(r"todo_list/",views.todo_store,name="todo_store"),
    path("delete_todo/<int:todo_id>/",views.delete_todo,name="delete_todos"),
 
]

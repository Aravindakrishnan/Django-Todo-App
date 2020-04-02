from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from app.models import Todo
# Create your views here.
def index(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request,"index.html",{"todo_items":todo_items})
@csrf_exempt
def todo_store(request):
    added_date1 = timezone.now()
    task1 = request.POST["task"]
    obj = Todo.objects.create(added_date=added_date1,text=task1)
    return HttpResponseRedirect("/")
@csrf_exempt
def delete_todo(request,todo_id):
    print("Deleted item id->",todo_id)
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")

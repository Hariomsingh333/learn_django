from django.shortcuts import redirect, render
from .forms import Todo_Form
from .models import Todo_data

# Create your views here.

# this is home and list the todo data
def index(req):
    main_data = Todo_data.objects.all()
    context={"data": main_data}
    return render(req,'index.html', context)

def create(req):
    form = Todo_Form()
    if req.method == 'POST':
        form = Todo_Form(req.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={"form": form}
    return render(req, 'create.html', context)

def update(req, pk):
    pk_todo = Todo_data.objects.get(id=pk)
    form = Todo_Form(instance=pk_todo)
    if req.method == 'POST':
        form = Todo_Form(req.POST, instance=pk_todo)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {"form": form}
    return render(req, 'create.html', context)

def delete(req, pk):
    pk_todo = Todo_data.objects.get(id=pk)
    if req.method == 'POST':
        pk_todo.delete()
        return redirect("/")
    context = {"item": pk_todo}
    return render(req, 'delete.html',context)
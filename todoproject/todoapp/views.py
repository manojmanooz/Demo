from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task
from .forms import todoform
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.
class TaskListView(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'task2'
class TAskDetailView(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'task2'
class TaskUpdateView(UpdateView):
    model=task
    template_name = 'update.html'
    context_object_name = 'task2'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class TaskDeleteView(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')




def home(request):
    task2=task.objects.all()
    if request.method == 'POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task1=task(name=name,priority=priority)
        task1.save()
    return render(request,'home.html',{'task2':task2})
def delete(request,todo_id):
    if request.method == 'POST':
        task3=task.objects.get(id=todo_id)
        task3.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,todo_id):
    tasks=task.objects.get(id=todo_id)
    form=todoform(request.POST or None,instance=tasks)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'tasks':tasks})
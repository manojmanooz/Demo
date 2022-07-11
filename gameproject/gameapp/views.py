from django.shortcuts import render, redirect
from .models import game
from .forms import gameform
# Create your views here.
def home(request):
    obj=game.objects.all()
    return render(request,'index.html',{'games':obj})
def detail(request,game_id):
    obj1=game.objects.get(id=game_id)
    return render(request, 'details.html', {'games1': obj1})
def add(request):
    if request.method == 'POST':
        name=request.POST.get('name',)
        decs=request.POST.get('dec')
        img=request.FILES['img']
        obj2=game(name=name,desc=decs,img=img)
        obj2.save()
    return render(request,'add.html')
def update(request,game_id):
    games=game.objects.get(id=game_id)
    form=gameform(request.POST or None,request.FILES,instance=games)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'games':games})
def delete(request,game_id):
    if request.method == 'POST':
        obj0=game.objects.get(id=game_id)
        obj0.delete()
        return redirect('/')
    return render(request,'delete.html')

















from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CreateForm
from .models import Creator

@login_required
def mypage(request):
    creator = request.user.creator
    
    return render(request, 'creator/mypage.html', {
        'creator': creator,
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('creator:login')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    
    return render(request, 'creator/signup.html',{
        'form': form
    })
    

def creators(request):
        
    creators = Creator.objects.all()
        
    return  render(request, 'creator/creators.html', {
        'creators': creators
    })
    
def creator(request, pk):
        
    creator = Creator.objects.get(pk=pk)
        
    return  render(request, 'creator/creator.html', {
        'creator': creator
    })
        

def edit(request):
    try:
        creator = request.user.creator
        
        if request.method == 'POST':
            form = CreateForm(request.POST, request.FILES, instance=creator)
            
            if form.is_valid():
                form.save()
                
                return redirect('core:index')
        else:
            form = CreateForm(instance=creator)        
    except Exception:
        if request.method == 'POST':
            form = CreateForm(request.POST, request.FILES)
            
            if form.is_valid():
                creator = form.save(commit=False)
                creator.user = request.user
                creator.save()
                
                return redirect('core:index')
        else:
            form = CreateForm()
    
    return render(request, 'creator/edit.html', {
        'form': form
    })

from django.shortcuts import render, redirect
from .models import List
from .forms import Listform
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):

    if request.method == 'POST':
        form= Listform(request.POST or None)

        if form.is_valid():
            form.save()
            all_items= List.objects.all
            messages.success(request,("item has been succesfully added"))
            return render(request, 'home.html',{'all_items':all_items})
        
    else:
        all_items= List.objects.all
        return render(request, 'home.html',{'all_items':all_items})

    
def about(request):
    return render(request, 'about.html',{})

def delete(request, List_id):
    item = List.objects.get(pk=List_id)
    item.delete()
    messages.success(request,("item has been deleted"))
    return redirect('home')

def cross(request, List_id):
    item = List.objects.get(pk=List_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, List_id):
    item = List.objects.get(pk=List_id)
    item.completed = False
    item.save()
    return redirect('home')


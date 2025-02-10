from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import TaskItem


def home(request):
	return render(request, 'todo/home.html')

def signupuser(request):
	if request.method == 'GET':
		return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
	else:
		if request.POST['password1'] == request.POST['password2']:
			try:
					user = 	User.objects.create_user(request.POST['username'],
					password=request.POST['password1'])
					user.save()
					login(request, user)
					return redirect('currenttodos')
			except IntegrityError:
				return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'User already exists'})
		else:
			return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'Password already exists'})
		
def loginuser(request):
	if request.method == 'GET':
		return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
	else:
			user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
			if user is None:
				return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(), 'error':'Username and password did not match'})
			else:
				login(request, user)
				return redirect('currenttodos')

def logoutuser(request):
	if request.method == 'POST':
		logout(request)
		return redirect('home')
	
def createtodo(request):
		if request.method == 'GET':
			return render(request, 'todo/createtodo.html', {'form':TodoForm()})
		else:
			try: 
				form = TodoForm(request.POST)
				newtodo = form.save(commit=False)
				newtodo.user = request.user
				newtodo.save()
				return redirect('currenttodos')
			except ValueError:
				return render(request, 'todo/createtodo.html', {'form':TodoForm(), 'error': 'Bad data passed in. Try Again'})
				
def currenttodos(request):
	todos = TaskItem.objects.filter(user=request.user, datecompleted__isnull = True)
	return render(request, 'todo/currenttodos.html', {'todos':todos})

def viewtodo(request, todo_pk):
	obj = get_object_or_404(TaskItem, pk=todo_pk, user=request.user)
	if request.method == 'GET':
		form = TodoForm(instance=obj)
		return render(request, 'todo/item_detail.html', {'object':obj, 'form':form})
	else:
			try:
				form = TodoForm(request.POST, instance=obj)
				form.save()
				return redirect('currenttodos') 
			except ValueError:
				return render(request, 'todo/item_detail.html', {'object':obj, 'form':form, 'error':'Bad info'})

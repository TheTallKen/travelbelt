
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import datetime
from django.contrib import messages
from .models import *

def index(request):
    dictionary = {
        'users' :  User.objects.all()
    }
    #for u in User.objects.all():
        #u.delete()
    return render(request, 'index.html')

def login(request):
    users = User.objects.all()
    for thing in users: 
        if request.POST['username'] == thing.username and request.POST['password'] == thing.password:
            u=User.objects.get(username=request.POST['username'])
            request.session['id']=u.id
            request.session['name']=u.name
    return redirect('/success')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        u= User.objects.create(name=request.POST['name'], username=request.POST['username'], password=request.POST['password'])
        request.session['id']=u.id
        request.session['name']=u.name
        return redirect('/success')

def success(request):
    dictionary  = {
        'travel' : Travel.objects.all(),
        'user' : User.objects.all(),
    }
    return render(request,'success.html', dictionary)

def add(request):
    return render(request, 'add.html')


def travel(request, id):
    b=Travel.objects.get(id=id)
    dictionary  = {
        'travel' : Travel.objects.all(),
        'user' : User.objects.all(),
    }
    return render(request, 'travel.html', dictionary)





#def addReview(request):
    #u=Book.objects.create(review=request.POST['review'], rating=request.POST['rating'],  user=User.objects.get(id=request.session['id']), book=Book.objects.get(id=request.session['id']))
    #return redirect('/books/addBook' + str(u.id))


#Validations aren't perfect, but it was impossible to find anything online about how to work with DateTimeField and we never covered it in a single assingment. So... I'm out of luck :) 
def addtravel(request):
    errors = Travel.objects.validate(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/add')
    else:
        t= Travel.objects.create(destination=request.POST['destination'], plans=request.POST['plans'], startdate=request.POST['startdate'],enddate=request.POST['enddate'], user=User.objects.get(id=request.session['id']))
        return redirect('/success')


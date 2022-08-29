from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import HttpResponse
from crud.models import Users

# Create your views here.


def show(request):
    users = Users.objects.all()
    context = {
        'users': users
    }

    return render(request, 'show.html', context)


@csrf_exempt
def insert(request):

    if request.method == "POST":
        id = request.POST['id']
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        data = Users(user_id=user_id, username=username,
                     firstname=firstname, lastname=lastname, email=email)
        data.save()
        return redirect('/info')
    else:
        return render(request, 'insert.html')


# update sql


def choiceUser(request):
    users = Users.objects.all()
    context = {
        'users': users
    }
    return render(request, 'selectuser.html', context)


@csrf_exempt
def update(request):
    users = Users()
    # show user choonse update
    if request.method == "GET":
        username = request.GET['username']
        users = Users.objects.get(username=username)
        context = {
            'users': users
        }
        return render(request, 'edit.html', context)


def edit(request, pk):
    users = Users.objects.get(id=pk)
    if request.method == "POST":
        redirect('/edit')
        id = request.POST['id']
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        users = Users(id=id, username=username,
                      firstname=firstname, lastname=lastname, email=email)
        users.save()
        return redirect('/info')
    else:
        context = {
            'users': users
        }
        return render(request, 'edit.html', context)


def deleteUser(request, pk):
    if request.method == "POST":
        users = Users.objects.get(id=pk)
        users.delete()
        return redirect('/info')
    else:
        return render(request, 'show.html')

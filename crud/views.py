from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
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
        user_id = request.POST['user_id']
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        data = Users(id=id, user_id=user_id, username=username,
                     firstname=firstname, lastname=lastname, email=email)
        data.save()

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
    # show user choonse update
    if request.method == "GET":
        username = request.GET['username']
        users = Users.objects.get(username=username)
        context = {
            'users': users
        }
        return render(request, 'edit.html', context)

    # update
    if request.method == "POST":
        users.username = request.POST['username']
        users.firstname = request.POST['firstname']
        users.lastname = request.POST['lastname']
        users.email = request.POST['email']

        users.save()
    template = loader.get_template('edit.html')
    return HttpResponse(template.render())

# delete

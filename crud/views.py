from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse
from crud.models import Users

# Create your views here.


def show(request):
    users = Users.objects.all()
    template = loader.get_template('show.html')
    return HttpResponse(template.render({'users': users}))


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

    template = loader.get_template('insert.html')
    return HttpResponse(template.render())

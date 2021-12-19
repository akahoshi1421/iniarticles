from django.utils import timezone
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from chat.models import Project

# Create your views here.
@login_required
def index(request):
    Project_data = Project.objects.all()
    data = {'Project_data': Project_data}
    return render(request, 'chat/index.html', data)

@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

@login_required
def project(request, project_id):
    return HttpResponse("project")

@login_required
def article(request, project_id, article_id):
    return HttpResponse("article")

@login_required
def make_project(request):
    data = {}
    my_on_public = False
    if request.method == 'POST':
        name = request.POST["name"]
        now_time = timezone.now()
        if "on_public" in request.POST:
            on_public = request.POST["on_public"]
            my_on_public = True
        result = Project(name = name, created_at = now_time, on_public = my_on_public)
        result.save()

    return render(request, 'chat/newproject.html')

@login_required
def make_article(request, project_id):
    return HttpResponse("make_article")

@login_required
def invite_project(request, project_id):
    return HttpResponse("invite_project")

@login_required
def invite_article(request, project_id, article_id):
    return HttpResponse("invite_article")

@login_required
def search_project(request):
    return HttpResponse("search_project")

@login_required
def search_article(request, project_id):
    return HttpResponse("search_article")

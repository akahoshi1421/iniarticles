from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    return render(request, 'chat/index.html', {})
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
    return HttpResponse("make_project")
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

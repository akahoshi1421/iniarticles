from django.utils import timezone
from django.shortcuts import redirect, render
from django.utils.safestring import mark_safe
from django.http import HttpResponse, JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from chat.models import Project, Article
import markdown

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
    data = {"prj_id": project_id}
    l = []
    articles = Article.objects.all()
    for article1 in articles:
        if article1.prj.id == project_id:
          l.append(article1)
    
    data["articles"] = l 
    return render(request, "chat/articles.html", data)

@login_required
def article(request, project_id, article_id):
    data = {"article_id": article_id, "prj_id": project_id}
    article_1 = Article.objects.get(id = article_id)
    article_result = {
        "update_at": str(article_1.update_at),
        "title": article_1.title
    }
    if article_1.content:
        article_result["content"] = article_1.content
        data["article_md"] = mark_safe(markdown.markdown(article_1.content))
    else:
        article_result["content"] = ""
        data["article_md"] = mark_safe("")

    data["article_1"] = article_result
    
    return render(request, "chat/article.html", data)

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
    data = {"prj_id": project_id}
    if request.method == "POST":
        name = request.POST["name"]
        new = Article(prj = Project(id = project_id), title = name)
        new.save()
        return redirect("project", project_id)

    return render(request, "chat/newarticle.html", data)

@login_required
def invite_project(request, project_id):
    return HttpResponse("invite_project")

@login_required
def invite_article(request, project_id, article_id):
    return HttpResponse("invite_article")

@login_required
def search_project(request):
    data = {}
    if request.method == "POST":
        content = request.POST["project_search"]
        results = Project.objects.filter(name = content)
        data["results"] = results
    return render(request, "chat/search_projects.html", data)


@login_required
def search_article(request, project_id):
    return HttpResponse("search_article")

from django.utils import timezone
from django.shortcuts import redirect, render
from django.utils.safestring import mark_safe
from django.http import HttpResponse, JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from chat.models import Project, Article
import markdown
from django.contrib.auth.models import User

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
    this_project = Project.objects.get(id = project_id)
    user_formated = myformat_serialize(this_project.allow_users)
    if not request.user.id in user_formated:
        return redirect("top")

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
    this_article = Article.objects.get(id = article_id)
    user_formated = myformat_serialize(this_article.allow_users)
    if not request.user.id in user_formated:
        return redirect("project", project_id)

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
        
        user = request.user.id#作成ユーザを取得し、そのユーザにアクセス権限を付与
        user_formated = str(user) + ","
        result = Project(allow_users = user_formated, name = name, created_at = now_time, on_public = my_on_public)
        result.save()
        return redirect("top")

    return render(request, 'chat/newproject.html')

@login_required
def make_article(request, project_id):
    data = {"prj_id": project_id}
    if request.method == "POST":
        name = request.POST["name"]
        user = request.user.id#作成ユーザを取得し、そのユーザにアクセス権限を付与
        user_formated = str(user) + ","
        new = Article(allow_users = user_formated, prj = Project(id = project_id), title = name)
        new.save()
        return redirect("project", project_id)

    return render(request, "chat/newarticle.html", data)

@login_required
def invite_project(request, project_id):
    data = {"prj": project_id}
    if request.method == "POST":
        invite_users = request.POST["invite_users"]
        invite_users += ","
        this_project = Project.objects.get(id = project_id)
        user_notformated = this_project.allow_users
        user_notformated += invite_users
        try:#ハッキング対策
            a = myformat_serialize(user_notformated)
            myformat_deserialize(a)
            this_project.allow_users = user_notformated
            this_project.save()
        except:
            return render(request, "chat/invite_project.html", data)


    return render(request, "chat/invite_project.html", data)

@login_required
def edit_project(request, project_id):
    data = {}
    if request.method == 'POST':
        try:
            this_project = Project.objects.get(id = project_id)
            if "btn_edit" in request.POST:
                this_project.name = request.POST["name"]
                #now_time = timezone.now() # 時間
                this_project.save()
                return redirect("top")
            
            elif "btn_delete" in request.POST:
                this_project.delete()
                return redirect("top")
        
        except:
            pass

    data = {"prj_id": project_id}
    return render(request, "chat/edit_project.html", data)

@login_required
def invite_article(request, project_id, article_id):
    data = {"prj": project_id, "article": article_id}
    if request.method == "POST":
        invite_users = request.POST["invite_users"]
        invite_users += ","
        this_article = Article.objects.get(id = article_id)
        user_notformated = this_article.allow_users
        user_notformated += invite_users
        try:#ハッキング対策
            a = myformat_serialize(user_notformated)
            myformat_deserialize(a)
            this_article.allow_users = user_notformated
            this_article.save()
        except:
            return render(request, "chat/invite_article.html", data)

    return render(request, "chat/invite_article.html", data)

@login_required
def search_project(request):
    data = {}
    if request.method == "POST":
        content = request.POST["project_search"]
        results = Project.objects.filter(name__icontains = content)
        data["results"] = results
    return render(request, "chat/search_projects.html", data)



@login_required
def exclude_project(request, project_id):
    data = {"prj": project_id}
    this_project = Project.objects.get(id = project_id)
    allow_users = this_project.allow_users
    allow_users_lists = myformat_serialize(allow_users)
    result = []
    for user in allow_users_lists:
        user_one = User.objects.get(id = user)
        user_one_dict = {"name": user_one.username, "id": user_one.id}
        result.append(user_one_dict)
    data["users_list"] = result

    if request.method == "POST":
        exclude_users = request.POST["exclude_users"]
        exclude_users += ","
        try:#ハッキング対策
            formated = myformat_serialize(exclude_users)
            if len(allow_users_lists) == 1:#アクセス権限がある人が1人だけである場合、権限を剝奪させないようにする
                return render(request, "chat/exclude_project.html", data)

            exclude_result = []
            for user in allow_users_lists:
                if not user in formated:
                    exclude_result.append(user)
            this_project.allow_users = myformat_deserialize(exclude_result)
            this_project.save()
        except:
            return render(request, "chat/exclude_project.html", data)
        return redirect("exclude_project", project_id)

    return render(request, "chat/exclude_project.html", data)

@login_required
def exclude_article(request, project_id, article_id):
    data = {"prj": project_id, "article": article_id}
    this_article = Article.objects.get(id = article_id)
    allow_users = this_article.allow_users
    allow_users_lists = myformat_serialize(allow_users)
    result = []
    for user in allow_users_lists:
        user_one = User.objects.get(id = user)
        user_one_dict = {"name": user_one.username, "id": user_one.id}
        result.append(user_one_dict)
    data["users_list"] = result

    if request.method == "POST":
        exclude_users = request.POST["exclude_users"]
        exclude_users += ","
        try:#ハッキング対策
            formated = myformat_serialize(exclude_users)
            if len(allow_users_lists) == 1:#アクセス権限がある人が1人だけである場合、権限を剝奪させないようにする
                return render(request, "chat/exclude_article.html", data)

            exclude_result = []
            for user in allow_users_lists:
                if not user in formated:
                    exclude_result.append(user)
            this_article.allow_users = myformat_deserialize(exclude_result)
            this_article.save()
        except:
            return render(request, "chat/exclude_article.html", data)
        return redirect("exclude_article", project_id, article_id)

    return render(request, "chat/exclude_article.html", data)

def myformat_serialize(string):#独自のフォーマットをリスト化
    result = []
    ichiji = ""
    for a in string:
        if a == ",":
            result.append(int(ichiji))
            ichiji = ""
        else:
            ichiji += a
    return result

def myformat_deserialize(lists):#独自のフォーマットを文字列化
    string = ""
    for b in lists:
        string += str(b)
        string += ","
    return string

@login_required
def search_article(request, project_id):
    data = {"prj_id": project_id}
    if request.method == "POST":
        content = request.POST["article_search"]
        results = Article.objects.filter(title__icontains = content,prj_id=project_id)
        data["results"] = results
    return render(request, "chat/search_article.html", data)

@login_required
@csrf_exempt
def project_api(request):
    if request.method == "POST":
        user_data = request.POST["user"]
        content = Project.objects.filter(name__icontains = user_data)
        l = []
        for a in content:
            if not a.name in l:
                l.append({"name":a.name,"id":a.id})
        data={"result":l}
        return JsonResponse(data)
    
    else:
        return HttpResponse("ERROR")

@csrf_exempt
def article_api(request,project_id):
    data = {"prj_id": project_id}
    if request.method == "POST":
        user_data = request.POST["user"]
        content = Article.objects.filter(title__icontains = user_data,prj_id=project_id)
        l = []
        for a in content:
            if not a.title in l:
                l.append({"title":a.title,"prj_id":a.prj_id,"id":a.id})
        data={"result":l}
        return JsonResponse(data)
    
    else:
        return HttpResponse("ERROR")
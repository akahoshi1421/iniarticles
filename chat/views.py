from django.http import request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from chat.models import Article
from django.http import HttpResponse, JsonResponse
import markdown

# Create your views here.
def top(request):
    return render(request ,"chat/index.html")

def room(request, room_name):
    data = {"room_name": room_name}
    return render(request, "chat/room.html", data)

@csrf_exempt
def make(request):
    if request.method == "POST":
        a = request.POST["data"]
        try:
            result = Article.objects.get(room_name = a)
        except:
            new = Article(text = "" ,room_name = a)
            new.save()
    
        result = Article.objects.get(room_name = a)
        data = {"data": result.text, "data_markdown":markdown.markdown(result.text)}
        return JsonResponse(data)
        
    return HttpResponse("ERROR")
from os import name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='top'),
    path('<int:project_id>/', views.project, name='project'),
    path('<int:project_id>/<int:article_id>/', views.article, name='article'),
    path('newproject/', views.make_project, name='make_project'),
    path('<int:project_id>/newarticle/', views.make_article, name='make_article'),
    path('<int:project_id>/invite/', views.invite_project, name='invite_project'),
    path('<int:project_id>/<int:article_id>/invite/', views.invite_article, name='invite_article'),
    path('searchproject/', views.search_project, name='search_project'),
    path('<int:project_id>/searcharticles/', views.search_article, name='search_article'),
    path("search/project", views.project_api, name="project_api"),
    path("<int:project_id>/search/article", views.article_api, name="article_api"),
]


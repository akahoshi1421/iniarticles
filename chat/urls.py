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
    path('<int:project_id>/edit/', views.edit_project, name='edit_project'),
    path('<int:project_id>/<int:article_id>/invite/', views.invite_article, name='invite_article'),
    path('<int:project_id>/exclude/', views.exclude_project, name='exclude_project'),
    path('<int:project_id>/<int:article_id>/exclude/', views.exclude_article, name='exclude_article'),
    path('searchprojects/', views.search_project, name='search_project'),
    path('<int:project_id>/searcharticles/', views.search_article, name='search_article'),
]


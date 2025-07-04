from django.urls import path
from . import views

urlpatterns = [
    path('project/', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/<int:pk>/vote/', views.vote_project, name='vote_project'),
    path('ranking/', views.project_ranking, name='project_ranking'),
]


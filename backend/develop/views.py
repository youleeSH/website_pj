from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Evaluation
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at develop index.")

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'develop/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'develop/project_detail.html', {'project': project})

def vote_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        value = int(request.POST.get("score"))
        Evaluation.objects.create(project=project, value=value)
        return redirect('project_detail', pk=pk)
    return redirect('project_detail', pk=pk)

def project_ranking(request):
    projects = Project.objects.all()
    sorted_projects = sorted(projects, key=lambda p: p.average_score(), reverse=True)
    return render(request, 'develop/project_ranking.html', {'projects': sorted_projects})

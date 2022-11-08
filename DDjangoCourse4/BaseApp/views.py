from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


# homepage
def projects(request):
    projects_obj = Project.objects.all()

    return render(request, 'BaseApp/projects.html', {'projects': projects_obj})


# single project page 
def project(request, pk):
    project_obj = Project.objects.get(id=pk)

    return render(request, 'BaseApp/project.html', {'project': project_obj})


# create project
def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    return render(request, "BaseApp/create-update.html", {'form': form})


# update project
def updateProject(request, pk):
    projectObj = Project.objects.get(id=pk)
    form = ProjectForm(instance=projectObj)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=projectObj)
        if form.is_valid():
            form.save()
            return redirect('projects')

    return render(request, "BaseApp/create-update.html", {'form': form})


# delete project
def deleteProject(request, pk):
    projectObj = Project.objects.get(id=pk)

    if request.method == 'POST':
        projectObj.delete()
        return redirect('projects')

    return render(request, 'BaseApp/delete-project.html', {'project': projectObj})
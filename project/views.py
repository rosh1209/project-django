from django.shortcuts import render, redirect
from .models import Project, Client, ProjectManager, EngineerRequirement
from .forms import ProjectForm, ClientForm, ProjectManagerForm, EngineerRequirementForm

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def project_manager_list(request):
    managers = ProjectManager.objects.all()
    return render(request, 'project_manager_list.html', {'managers': managers})

def engineer_requirement_list(request):
    requirements = EngineerRequirement.objects.all()
    return render(request, 'engineer_requirement_list.html', {'requirements': requirements})

def home(request):
    return render(request, 'home.html')


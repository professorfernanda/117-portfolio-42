from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


# Function-based views
def project_list(request):

    projects = Project.objects.all()

    return render(request, "content/project_list.html", {"projects": projects})


def project_new(request):

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            return redirect('project_list') 
    else:
        form = ProjectForm()

    return render(request, 'content/project_new.html', {
        'form' : form
    })

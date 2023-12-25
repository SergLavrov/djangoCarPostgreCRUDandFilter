from django.shortcuts import render

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect

# from .forms import ProjectCreateForm, ProjectFilterForm, ProjectUpdateForm

# from .models import Project, User

# Create your views here.

def create_car(request: HttpRequest) -> HttpResponse:

    # Получение заполненой формы
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            project = Project()
            project.title = form.cleaned_data['title']
            project.description = form.cleaned_data['description']
            project.email = form.cleaned_data['email']
            project.countUser = form.cleaned_data['countUser']
            project.save()

            return HttpResponseRedirect("/project/")
    # Получение формы для заполнения
    else:
        form = ProjectCreateForm()
    return render(
        request,
        'project/CreateProject.html',
        {'form': form}
    )
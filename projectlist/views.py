from django.shortcuts import render,get_object_or_404,redirect
from .models import Project,Rating

# Create your views here.

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projectlist/project_list.html', {'projects': projects})
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':
        score = int(request.POST.get('score'))
        Rating.objects.create(project=project,score=score)
        return redirect('projectlist:project_detail',project_id=project.id)

    average = project.average_rating() if request.user.is_staff else None

    
    return render(request,'projectlist/project_detail.html',{
        'project':project,
        'average':average,
    })

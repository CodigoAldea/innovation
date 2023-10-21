from django.shortcuts import render, get_object_or_404
from .models import Branches,Project
from django.views.generic import ListView
from .models import Contact
from django.core.paginator import Paginator


def project_list(request, pk):
    branch = Branches.objects.get(name=pk)
    projects = Project.objects.filter(branch=branch)
    items_per_page = 12  # Adjust as needed
    paginator = Paginator(projects, items_per_page)
    page_number = request.GET.get('page')

    # Get the Page object for the current page
    page = paginator.get_page(page_number)
    return render(request, 'data.html', {'page': page, 'branch': branch})

def pro_detail(request,pk):
    # branch=Branches.objects.get(name=pk)
    projects=Project.objects.filter(title=pk)
    project = projects.first()
    branch_name = project.branch.name
    return render(request, 'newww.html', {'detail': projects, 'branch':branch_name})

class ContactListView(ListView):
    model = Contact
    template_name = 'contact_list.html'
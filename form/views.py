from django.shortcuts import render, get_object_or_404
from .models import Branches,Project
from django.views.generic import ListView
from .models import Contact


def project_list(request,pk):
    branch=Branches.objects.get(name=pk)
    projects=Project.objects.filter(branch=branch)
    return render(request, 'data.html', {'projects': projects})

def pro_detail(request,pk):
    # branch=Branches.objects.get(name=pk)
    projects=Project.objects.filter(title=pk)
    project = projects.first()
    branch_name = project.branch.name
    return render(request, 'newww.html', {'detail': projects, 'branch':branch_name})

class ContactListView(ListView):
    model = Contact
    template_name = 'contact_list.html'
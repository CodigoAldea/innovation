from django.shortcuts import render, redirect
from django.contrib import messages
from form.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from form.forms import ContactForm
from django.shortcuts import get_object_or_404





def home(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        mail=updates(email=email)
        mail.save()
    return render(request,"index.html")

"""def AIML(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        mail=updates(email=email)
        mail.save()
    return render(request, "AIML.html")"""

def certification(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        mail=updates(email=email)
        mail.save()
    return render(request, "Certification.html")

"""def CI(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        mail=updates(email=email)
        mail.save()
    return render(request, "CI.html")"""

def contact(request):
    if request.method == 'POST':
        # Handling the contact form submission
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        email = request.POST.get('email')

        if name and email:  # Ensure that name and email are provided
            new_contact = Contact(name=name, email=email, phone=phone, message=message)
            new_contact.save()
            messages.success(request, 'Your message has been sent successfully!')

        # Handling the email updates form submission
        update_email = request.POST.get('email')
        if update_email:
            # Create a new updates instance and save it only if email is provided
            mail = updates(email=update_email)
            mail.save()
    
    return render(request, 'contact.html')

"""def cs(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        mail=updates(email=email)
        mail.save()
    return render (request, "CS.html")"""

"""def electrical(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        mail=updates(email=email)
        mail.save()
    return render (request,"Electrical.html")"""

"""def electronic(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        mail=updates(email=email)
        mail.save()
    return render (request, "Electronic.html")"""

"""def emedico(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        mail=updates(email=email)
        mail.save()
    return render(request, "emedico.html")"""

"""def about(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        mail=updates(email=email)
        mail.save()
    return render(request, "about.html")"""

def intern(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        mail=updates(email=email)
        mail.save()
    return render (request, "Internships.html")

"""def iot(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        mail=updates(email=email)
        mail.save()
    return render (request, "IoT.html")"""

def projects(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        mail=updates(email=email)
        mail.save()
    return render(request, "Projects.html")

def Regis(request):
    LastInsertId = (Register.objects.last()).id
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        branch=request.POST.get('branch')
        topic=request.POST.get('topic')
        query=request.POST.get('query')
        degree=request.POST.get('degree')
        # regis instance
        if name and email:
            new_regis=Register(name=name,
                email=email,
                phone=phone,
                branch=branch,
                topic=topic,
                query=query,
                degree=degree)
            new_regis.save()
            messages.success(request, 'Your message has been sent successfully!')

        # Handling the email updates form submission
        update_email = request.POST.get('email')
        if update_email:
            # Create a new updates instance and save it only if email is provided
            mail = updates(email=update_email)
            mail.save()
    return render(request,"Registeration.html",{'data':LastInsertId})

def resources(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        mail=updates(email=email)
        mail.save()
    return render(request,"Resources.html")

"""def robotics(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        mail=updates(email=email)
        mail.save()
    return render(request, "Robotics.html")"""


def adminbase(request):
    return render(request, 'a_home.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('/dashboard/')
            else:
                messages.error(request, 'You do not have admin privileges.')
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'login.html')

def aquery_detail(request):
    item= Register.objects.all().order_by('-id')
    if request.method =='POST' :
        name=request.POST.get('name')
        email=request.POST.get('email')
        degree=request.POST.get('degree')
        phone=request.POST.get('phone')
        branch=request.POST.get('branch')
        topic=request.POST.get('topic')
        query=request.POST.get('query')
        if name:
            a = Register.objects.create(name=name, email=email, degree=degree, phone= phone, branch=branch, topic=topic, query=query)
            a.save()
        return render(request, 'a_querydetail.html',{'data': item})
    return render(request, 'a_querydetail.html',{'data': item})

def delquery(request,pk):
    item=Register.objects.get(pk=pk)
    item.delete()
    return redirect('q_dash')

def abranches(request):
    item=Branches.objects.all().order_by('-id')
    if request.method == 'POST':
        name=request.POST.get('name')
        if name:
            a=Branches.objects.create(name=name)
            a.save()
        return render(request, 'a_branch.html',{'data': item})
    return render(request, 'a_branch.html',{'data': item})

def delbranch(request,pk):
    item=Branches.objects.get(pk=pk)
    item.delete()
    return redirect ('branch_dash')

def astudent_detail(request):
    item=Contact.objects.all().order_by('-id')
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        if name:
            a=Contact.objects.create(name=name, email=email, phone= phone, message=message)
            a.save()
        return render(request, 'a_studentdetail.html',{'data': item})
    return render(request, 'a_studentdetail.html',{'data': item})

def delstudent(request,pk):
    item=Contact.objects.get(pk=pk)
    item.delete()
    return redirect ('stu_dash')

def aemail_updates(request):
    item=updates.objects.all().order_by('-id')
    if request.method == 'POST':
        email=request.POST.get('email')
    return render(request, 'a_emailupdates.html',{'data': item})

def delemail(request, pk):
    try:
        item = get_object_or_404(updates, pk=pk)
        item.delete()
        return redirect('email_dash')
    except updates.DoesNotExist:
        # Handle the case where the updates object with the specified primary key doesn't exist
        # You can return an error page or redirect as needed
        return HttpResponse("Email updates not found", status=404)

def aproject(request):
    item=Project.objects.all().order_by('-id')
    b=Branches.objects.all()
    if request.method == 'POST':
        title=request.POST.get('title')
        image=request.FILES.get('image')
        image2=request.FILES.get('image2')
        branch=request.POST.get('branch')
        branch_name = get_object_or_404(Branches, name=branch)
        description=request.POST.get('description')
        components=request.POST.get('components')
        application_area=request.POST.get('application_area')
        a=Project.objects.create(
            title=title,image=image,image2=image2,branch=branch_name, description=description, components=components, application_area=application_area 
            )
        a.save()
        return render(request, 'a_projects.html',{'data': item, 'branch':b})
    return render(request, 'a_projects.html',{'data': item ,'branch':b })

def delproject(request,pk):
    item=Project.objects.get(pk=pk)
    item.delete()
    return redirect ('pro_dash')

def admin_logout(request):
    logout(request)
    return redirect('/login/') 

def edit_project(request, pk):
    branch = Branches.objects.all()
    project = Project.objects.get(pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        branch_name = request.POST.get('branch')
        description = request.POST.get('description')
        components = request.POST.get('components')
        application_area = request.POST.get('application_area')
        
        image = request.FILES.get('image')
        image2 = request.FILES.get('image2')

        branch_instance = Branches.objects.get(name=branch_name)
        project.title = title
        project.branch = branch_instance
        project.description = description
        project.components = components
        project.application_area = application_area

        if image:
            project.image = image
        if image2:
            project.image2 = image2

        project.save()

        return redirect('pro_dash')  # Redirect to the appropriate URL after updating

    return render(request, 'edit_pro.html', {'projects': project, 'branch': branch})
"""
URL configuration for innovation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from innovation import views
# for media and upload images 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('certification/',views.certification),
    path('contact/',views.contact),
    path('intern/',views.intern),
    path('project/',views.projects),
    path('register/',views.Regis),
    path('resources/',views.resources),
    path('dashboard/',views.adminbase),
    path('dashboard/branch',views.abranches, name='branch_dash'),
    path('dashboard/bdel/<int:pk>',views.delbranch),
    path('dashboard/mcheck',views.aproject, name='pro_dash'),
    path('dashboard/edit_project/<int:pk>', views.edit_project, name='edit_project'),
    path('dashboard/pdel/<int:pk>',views.delproject),
    path('dashboard/mform',views.aquery_detail, name='q_dash'),
    path('dashboard/dele/<int:pk>',views.delquery),
    path('dashboard/auser',views.astudent_detail, name='stu_dash'),
    path('dashboard/sdel/<int:pk>',views.delstudent),
    path('dashboard/amail',views.aemail_updates, name='email_dash'),
    path('dashboard/edel/<int:pk>',views.delemail),
    path('login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('img/',include('form.urls')), # for the app form
    path('dashboard/edit_query/<int:pk>', views.editquery, name='edit_query'), # added by amit
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # to route the uplaod images

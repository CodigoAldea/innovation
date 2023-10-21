from django.urls import path 
from .import views
from form.views import project_list, pro_detail

urlpatterns = [
    path('projects/<str:pk>', views.project_list),
    path('ptitle/<str:pk>', views.pro_detail),
]

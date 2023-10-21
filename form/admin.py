from django.contrib import admin
from form.models import Contact,Register,updates,Branches,Project

# Register your models here.

class contactAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','message']
admin.site.register(Contact,contactAdmin)


class registerAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','branch','topic','query','degree']
admin.site.register(Register,registerAdmin)

class updatesAdmin(admin.ModelAdmin):
    list_display=['email']
admin.site.register(updates,updatesAdmin)

class BranchAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Branches,BranchAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display=['title','image','image2','branch','description','components','application_area']
admin.site.register(Project,ProjectAdmin)
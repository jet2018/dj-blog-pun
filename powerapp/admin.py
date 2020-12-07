from django.contrib import admin

# Register your models here.
from .models import Gallery, About, AboutTheParty, Achievement, Prospective, Candidate, Blog


def publish_post(modeladmin, request, queryset):
	queryset.update(is_published=True)
	publish_post.short_description ='Publish selected stories to show them live on the website'

# def apply_Changes(modeladmin, request, queryset):
#     queryset.update(Use_New_App_Name =True)
#     queryset.update(Use_New_What_We_Do = True)
#     queryset.update(Use_New_Where_We_Are = True)
#     queryset.update(Use_New_Goals = True)
#     queryset.update(Use_New_Vision = True)
#     apply_Changes.short_description ='Publish your new settings on the site'

# def Un_apply_Changes(modeladmin, request, queryset):
#     queryset.update(Use_New_App_Name =False)
#     queryset.update(Use_New_What_We_Do = False)
#     queryset.update(Use_New_Where_We_Are = False)
#     queryset.update(Use_New_Goals = False)
#     queryset.update(Use_New_Vision = False)
#     Un_apply_Changes.short_description ='Publish your new settings on the site'


def Un_Publish(modeladmin, request, queryset):
	queryset.update(is_published=False)
	Un_Publish.short_description ='Un publish selected posts to stop them from running on the website'

class GalleryAdmin(admin.ModelAdmin):
    actions =[publish_post, Un_Publish]
    list_display=('short_description','is_published','upload_date',)
    list_filter = ['added_by', 'is_published', 'upload_date']
    ordering =['-upload_date']


# class AboutAdmin(admin.ModelAdmin):
#     actions = [apply_Changes, Un_apply_Changes]
#     list_display=('AppName','Use_New_App_Name','Use_New_App_Name','Use_New_What_We_Do','Use_New_Where_We_Are','Use_New_Goals','Use_New_Vision',)



class BlogAdmin(admin.ModelAdmin):
    actions = [publish_post, Un_Publish]
    list_display=('title','added_by','is_published','upload_date')
    list_filter =['is_published', 'upload_date']

class CandidateAdmin(admin.ModelAdmin):
    actions = [publish_post, Un_Publish]
    list_display=('full_name','added_by','is_published','upload_date')
    ordering =['-upload_date']
    list_filter = ['is_published', 'upload_date']

admin.site.register(About)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(AboutTheParty)
admin.site.register(Prospective)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Achievement)
admin.site.register(Candidate, CandidateAdmin)

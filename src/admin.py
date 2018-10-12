from django.contrib import admin
from .models import *
from .actions import export_as_csv_action


#from import_export.admin import ImportExportModelAdmin
# Register your models here.
class core_team_model(admin.ModelAdmin):
    list_display=["name","post","fb_link","git_link","linkedin_link"]
    class Meta:
        model=Secretarie
class about_us_model(admin.ModelAdmin):
    list_1=["text","img"]
    class Meta:
        model=About_us
class event_model(admin.ModelAdmin):
    list_2=["logo","heading","description"]
    class Meta:
        model=Events

class team_model(admin.ModelAdmin):
	list_display=["name","department"]
	list_filter=["department"]
	class Meta:
		model=Team

class post_model(admin.ModelAdmin):
	list_display=["title","timestamp"]
	date_hierarchy = 'timestamp'
	search_fields = ['title','content']
	class Meta:
		model=Post

class msweek_event_model(admin.ModelAdmin):
	list_display=["title","date"]
	date_hierarchy = 'date'
	search_fields = ['title','description']
	class Meta:
		model=MSWeek_Event

class inspirus_event_model(admin.ModelAdmin):
	list_display=["title","date"]
	date_hierarchy = 'date'
	search_fields = ['title','description']
	class Meta:
		model=Inspirus_Event

class rumble_event_model(admin.ModelAdmin):
	list_display=["title","date"]
	date_hierarchy = 'date'
	search_fields = ['title','description']
	class Meta:
		model=Rumble_Event


class head_model(admin.ModelAdmin):
    list_display=["name","department","post"]
    list_filter=["department","post"]
    class Meta:
        model=Head_Team

@admin.register(event_registration)
class EventRegistration_model(admin.ModelAdmin):
    list_display=["name","year","email"]
    # list_filter=["a","b","c","d","e","year"]
    list_filter=["year"]
    # actions = [export_as_csv_action("CSV Export", fields=['name','year','email','contact','a','b','c','d','e'])]
    actions = [export_as_csv_action("CSV Export", fields=['name','email','contact','year'])]

@admin.register(registration)
class registration_model(admin.ModelAdmin):
    list_display=["name","year","email"]
    # list_filter=["a","b","c","d","e","year"]
    list_filter=["a","b","year"]
    # actions = [export_as_csv_action("CSV Export", fields=['name','year','email','contact','a','b','c','d','e'])]
    actions = [export_as_csv_action("CSV Export", fields=['name','email','roll_number','contact','year','a','b'])]

@admin.register(hkct_register)
class hkct_model(admin.ModelAdmin):
    list_display=["name","year"]
    # list_filter=["a","b","c","d","e","year"]
    list_filter=["a","b","c","d","e","f","year"]
    # actions = [export_as_csv_action("CSV Export", fields=['name','year','email','contact','a','b','c','d','e'])]
    actions = [export_as_csv_action("CSV Export", fields=['name','email','contact','year','a','b','c','d','e','f'])]

@admin.register(hkct_ouside)
class hkct_model(admin.ModelAdmin):
    list_display=["name","location"]
    # list_filter=["a","b","c","d","e","year"]
    list_filter=["location", "institute"]
    # actions = [export_as_csv_action("CSV Export", fields=['name','year','email','contact','a','b','c','d','e'])]
    actions = [export_as_csv_action("CSV Export", fields=['name','email','contact','location','institute'])]

class Contact_request(admin.ModelAdmin):
    list_display=["contact_name","contact_email"]

admin.site.register(Secretarie,core_team_model)
admin.site.register(Head_Team,head_model)
admin.site.register(About_us,about_us_model)
admin.site.register(About_us_content)
admin.site.register(Events,event_model)
admin.site.register(Post,post_model)
admin.site.register(Team,team_model)
admin.site.register(MSWeek_Event,msweek_event_model)
admin.site.register(Inspirus_Event,inspirus_event_model)
admin.site.register(Rumble_Event,rumble_event_model)
admin.site.register(contact_request,Contact_request)
admin.site.register(index_gallery)
admin.site.register(MSWEEK_gallery)
admin.site.register(INSPIRUSUS_gallery)
admin.site.register(RUMBLE_gallery)
admin.site.register(Heading_Content)
# admin.site.register(registration)
# admin.site.register(registration,registration_model)

from django.contrib import admin
from .models import AccessRecord, Topic, Webpage

# Register your models here.
class TopicAdmin(admin.ModelAdmin):
	list_display = ('name')


class WebpageAdmin(admin.ModelAdmin):
	list_display= ('topic', 'name', 'url')


class AccessRecordAdmin(admin.ModelAdmin):
	list_display = ('name', 'date')


admin.site.register(AccessRecord, AccessRecordAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Webpage, WebpageAdmin)

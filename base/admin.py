from django.contrib import admin
from .models import Job, About, Skill, Achievement, Item
from embed_video.admin import AdminVideoMixin


admin.site.register(Job)
admin.site.register(About)
admin.site.register(Achievement)
admin.site.register(Skill)

# Register your models here.



class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)
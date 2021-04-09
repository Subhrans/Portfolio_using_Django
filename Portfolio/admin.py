from django.contrib import admin
from .models import (MyDetail,
                     Project,
                     Achievment,
                     Social_Site_Connection,
                     Subscribe,
                     ContactUs,
                     MailBackend,
                     Language,
                     )


# Register your models here.
@admin.register(MyDetail)
class MyDetailAdmin(admin.ModelAdmin):
    # fields = ['id','url']
    list_display = ['id', 'url', 'user', 'slug']
    list_display_links = ['id', 'user', 'slug']
    # prepopulated_fields = {"url":('id',)}


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'slug']
    list_display_links = ['name', 'id', 'slug']
    # prepopulated_fields = {"slug":('name','language_used','created_date')}


admin.site.register(Project, ProjectAdmin)

admin.site.register(Language)
admin.site.register(Achievment)
admin.site.register(Subscribe)
admin.site.register(Social_Site_Connection)
admin.site.register(ContactUs)
admin.site.register(MailBackend)

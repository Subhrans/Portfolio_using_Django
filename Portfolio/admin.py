from django.contrib import admin
from .models import (MyDetail,
                     Project,
                     Achievment,
                     Social_Site_Connection,
                     Subscribe,
                     ContactUs,
                     MailBackend,
                     )

# Register your models here.
@admin.register(MyDetail)
class MyDetailAdmin(admin.ModelAdmin):
    # fields = ['id','url']
    list_display = ['id','url','user','slug']
    list_display_links = ['id','user','slug']
    # prepopulated_fields = {"url":('id',)}
# admin.site.register(MyDetail)


admin.site.register(Project)
admin.site.register(Achievment)
admin.site.register(Subscribe)
admin.site.register(Social_Site_Connection)
admin.site.register(ContactUs)
admin.site.register(MailBackend)

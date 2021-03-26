from django.contrib import admin
from .models import (MyDetail,
                     Under_Graduation,
                     Project,
                     Qualification,
                     Achievment,
                     Social_Site_Connection,
                     Secondary_Examination,
                     Higher_Secondary_Examination,
                     Post_Graduation,
                     Subscribe,

            )
# Register your models here.
admin.site.register(MyDetail)
admin.site.register(Under_Graduation)
admin.site.register(Project)
admin.site.register(Qualification)
admin.site.register(Achievment)
admin.site.register(Social_Site_Connection)
admin.site.register(Secondary_Examination)
admin.site.register(Higher_Secondary_Examination)
admin.site.register(Post_Graduation)
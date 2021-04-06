from django.contrib import admin
from .models import (MyDetail,
                     Project,
                     Achievment,
                     Social_Site_Connection,
                     Subscribe,
                     Pics,
                     ContactUs,
                     MailBackend,
                     )

# Register your models here.
admin.site.register(MyDetail)
admin.site.register(Project)
admin.site.register(Achievment)
admin.site.register(Pics)
admin.site.register(Subscribe)
admin.site.register(Social_Site_Connection)
admin.site.register(ContactUs)
admin.site.register(MailBackend)

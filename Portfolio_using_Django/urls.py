from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Portfolio Admininstration"
admin.site.site_title = "PORTFOLIO"
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include('allauth.urls')),
                  path('', include('Portfolio.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

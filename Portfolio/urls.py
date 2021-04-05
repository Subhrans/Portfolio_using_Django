from django.urls import path
from .views import index, contact_us_view

app_name = "portfolio"
urlpatterns = [
    path('', index, name="index"),
    path('contact_us/', contact_us_view, name="contact_us"),
]

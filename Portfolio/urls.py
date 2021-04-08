from django.urls import path
from . import views

app_name = "portfolio"
urlpatterns = [
    path('', views.index, name="index"),
    path('contact_us/', views.contact_us_view, name="contact_us"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
]

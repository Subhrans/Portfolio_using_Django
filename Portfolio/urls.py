from django.urls import path
from .views import *

app_name = "portfolio"
urlpatterns = [
    path('', index, name="index"),
    path('<str:username>/', portfolio_view, name="user_portfolio_view"),
    # path('<str:username>/', contact_us_view, name="user_portfolio_view"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('contact_us/en/', contact_us_view, name="contact_us"),
    path('<userid>/contact_us/en/', contact_us_view, name="contact_us"),
]

from django.urls import path
from .views import index,base_view
urlpatterns=[
    path('',base_view,name="base_view"),
    path('home/',index,name="index"),
]
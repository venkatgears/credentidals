from django.urls import path
from .views import createView , show_users , homeView

urlpatterns = [
    path('',homeView),
    path('create/',createView),
    path('show/',show_users),
]

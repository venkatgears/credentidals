from django.urls import path
from .views import home_view, show_users, create_view

urlpatterns = [
    path("", home_view, name="home"),
    path("create/", create_view, name="create"),
    path("show/", show_users, name="show"),
]

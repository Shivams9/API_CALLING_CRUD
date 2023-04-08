from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('admin/', admin.site.urls),

    path("create", views.create),
    path("read", views.read),
    path("edit", views.edit),
    path("delete", views.delete),
    path("update", views.update),
    path("jsonall", views.jsonall),

]

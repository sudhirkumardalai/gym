from django.contrib import admin
from django.urls import path
from service import views

urlpatterns = [
    path('home/',views.home),
    path('',views.test),

    path('delete/<id>',views.delete),
    path('update/<id>',views.update),
    path('log/',views.log),
    path('logo/',views.logo),
    path('register/',views.register),
    path('admin/', admin.site.urls),
]
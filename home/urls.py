from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
 path("",views.index, name='home'),
 path("services", views. services, name='services'),
 path("blog", views.blog, name='blog'),
 path("contact", views.contact_view, name='contact'),
 path("contact me", views.contact_view, name='contact me'),
 path("intro", views.intro, name='intro'),
]

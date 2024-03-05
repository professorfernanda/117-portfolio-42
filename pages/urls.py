from django.urls import path
from pages import views

urlpatterns = [
    path("contact", views.contact_view, name="contact"),
    path("", views.about_view, name="about"),
]

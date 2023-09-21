from django.urls import path
from recipes.views import home, about, contact

urlpatterns = [
    path("", home, name="home"),  # Home
    path("about/", about, name="about"),  # About
    path("contact/", contact, name="contact"),  # Contact
]

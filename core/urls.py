from django.urls import path
from core.views import *

urlpatterns = [
    path("",home, name="home"),

    path("about/",about, name="about"),

    path("services/residential/",residential, name="residential"),

    path("services/commercial/", commercial, name="commercial"),

    path("services/villa/", villa , name="villa"),

    path("services/planning/", planning, name="planning"),

    path("services/furniture/", furniture, name="furniture"),

    path("contact/",contact,name="contact"),

    path(
        "consultation/",
        consultation,
        name="consultation"
    ),

]
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("post_list",views.post_list, name="post_list"),
    path("about",views.about,name="About"),
    path("contact",views.contact,name="Contact"),
    path("news",views.news,name="News"),
    path("faqs",views.faqs, name="FAQs")
]

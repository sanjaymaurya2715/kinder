

from django.urls import path
from . import views

urlpatterns = [
path("",views.home, name="home"),
path("register/",views.register, name="register"),
path("login/",views.login,name="login"),
path("hindi_alphabet/",views.hindi_alphabet,name="hindi_alphabet"),
path("english_alphabet/",views.english_alphabet,name="english_alphabet"),
path("numbers/",views.numbers,name="numbers"),
path("animals/",views.animals,name="animals"),
path("parent_dashboard/",views.parent_dashboard,name="parent_home"),
path("parent_feedback/",views.parent_feedback,name="parent_feedback"),
path("contact_us/",views.contact,name="contact"),
path("color/",views.color,name="color"),
path("parent_edit_profile/",views.parent_edit_profile,name="parent_edit_profile"),
path("gallery/",views.gallery,name="gallery"),
path("about_us/",views.about_us,name="about_us"),
path("logout/",views.parent_logout,name="parent_logout"),
path("story/",views.story,name="story"),
path("poem/",views.poem,name="poem"),


# path('user_home/',views.user_home,name="user_home")
]

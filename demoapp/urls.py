from django.urls import path 
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("demo/",views.demo,name="demo"),
    path("bhavani/",views.bhavani,name="bhavani"),
    path("sree/",views.sree,name="sree"),
]
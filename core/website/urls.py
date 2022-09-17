from django.urls import path
from .views import *

urlpatterns = [
    path('',homepage,name='homepage'),
    path('about/',aboutUs,name='aboutus'),
    path('contact/',contactUs,name='contactus'),
    path('blog/',blog,name='blog'),
    path('blog_detail/<int:id>',blog_detail,name='blog_detail'),
    path('gallery',gallery,name='gallery'),
    path('projects/',projects,name='projects'),
    path('careers/',careers,name='careers'),
    path('for_developers/',for_developers,name='for_developers'),
    path('press/',press,name='press'),
    path('programs/',programs,name='programs'),
    path('publications/',publications,name='publications'),
    path('resources/',resources,name='resources'),
    path('faqs/',faqs,name='faqs'),
    path('stakeholders/',stakeholders,name='stakeholders'),
    path('team/',team,name='team'),
    path('team_detail/',team_detail,name='team_detail'),

    path('projects/kyb',kyb,name='kyb'),
    path('projects/marble',marble,name='marble'),
    path('projects/eom',eom,name='eom'),

]

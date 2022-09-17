from django.urls import path
from .views import *

urlpatterns = [
    path('',dashboard_home,name='dashboard-home'),
    path('projects/',dashboard_projects,name='dashboard-projects'),
    path('gallery/',dashboard_gallery,name='dashboard-gallery'),
    path('blog/',dashboard_blog,name='dashboard-blog'),
    path('mailing_list/',dashboard_mailing_list,name='dashboard-mailing_list'),
    path('procurement/',dashboard_procurement,name='dashboard-procurement'),
    path('inventory/',dashboard_inventory,name='dashboard-inventory'),
    path('register/',dashboard_register,name='dashboard-register'),
    path('stakeholder/',dashboard_stakeholders,name='dashboard-stakeholders'),
    path('website/',dashboard_website,name='dashboard-website'),

    path('staffs/',dashboard_staffs,name='dashboard_staffs'),

    path('homepage/',dashboard_homepage,name='dashboard-homepage'),
    path('contactus/',dashboard_contactus,name='dashboard-contactus'),
    path('aboutus/',dashboard_aboutus,name='dashboard-aboutus'),
    path('faq/',dashboard_faq,name='dashboard-faq'),
    path('team/',dashboard_team,name='dashboard-team'),
    path('footer/',dashboard_footer,name='dashboard-footer'),
    path('career/',dashboard_career,name='dashboard-career'),
    path('testimonials/',dashboard_testimonials,name='dashboard-testimonials'),

    path('register/',registerPage,name="register"),
    path('login/',loginUser,name="login"),
    path('logout/',logoutUser,name="logout"),
]

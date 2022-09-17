from django.shortcuts import render
from blog.models import Post, Category
from cms.models import *


def homepage(request):
    testimonials = Testimonials.objects.all()
    categories = Category.objects.all()
    posts      = Post.objects.all()

    obj = Post()
    published_date = obj.get_published_date()

    context = {
        'testimonials':testimonials,
        'categories':categories,
        'posts':posts,
        'published_date':published_date,
    }
    return render(request,'website/pages/homepage.html',context)


def aboutUs(request):
    return render(request,'website/pages/about-us.html')


def contactUs(request):
    contact = Contact.objects.last()
    context = {
        'contact':contact
    }
    return render(request,'website/pages/contact-us.html',context)


def blog(request):
    categories = Category.objects.all()
    posts      = Post.objects.all()

    obj = Post()
    published_date = obj.get_published_date()

    context = {
        'categories':categories,
        'posts':posts,
        'published_date':published_date,
    }

    return render(request,'website/pages/blog.html',context)


def blog_detail(request,id):
    post = Post.objects.get(id=id)

    context = {
        'post':post,
    }

    return render(request,'website/pages/blog_detail.html',context)


def projects(request):
    return render(request,'website/pages/projects.html')


def gallery(request):
    return render(request,'website/pages/gallery.html')


def careers(request):
    careers = Careers.objects.all()

    context = {
        'careers' : careers,
    }

    return render(request,'website/pages/careers.html',context)


def for_developers(request):
    return render(request,'website/pages/for-developers.html')


def press(request):
    return render(request,'website/pages/press.html')


def programs(request):
    return render(request,'website/pages/programs.html')


def publications(request):
    return render(request,'website/pages/publications.html')


def resources(request):
    return render(request,'website/pages/resources.html')


def faqs(request):
    faqs = Faqs.objects.all()
    context = {
        'faqs' : faqs,
    }
    return render(request,'website/pages/faqs.html', context)


def stakeholders(request):
    return render(request,'website/pages/stakeholders.html')


def team(request):
    teams = Team.objects.all()

    context = {
        'teams':teams,
    }
    return render(request,'website/pages/team.html',context)


def team_detail(request):
    return render(request,'website/pages/team_detail.html')


def kyb(request):
    return render(request,'website/pages/projects/kyb.html')


def marble(request):
    return render(request,'website/pages/projects/marble.html')


def eom(request):
    return render(request,'website/pages/projects/eom.html')
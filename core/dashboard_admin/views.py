from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings


#from gp_about.models import Staff
from projects.models import Projects
from projects.forms import ProjectForm
from inventory.models import Inventory
from inventory.forms import InventoryForm
from cms.models import *
from cms.forms import ContactForm, FooterForm, FaqsForm, CareerForm, TestimonialsForm, TeamsForm
from blog.models import Post
from blog.forms import PostForm
from index.models import *
from index.forms import SliderForm, WhatWeDoForm, AboutUsForm


@login_required(login_url='login')
def dashboard_home(request):
    slider_form = SliderForm()
    whatwedo_form = WhatWeDoForm()
    aboutus_form = AboutUsForm()

    if request.method == 'POST':
        if 'slider_form' in request.POST:
            slider_form = SliderForm(request.POST)
            if slider_form.is_valid():
                slider_form.save()
                messages.success(request, 'Slider Added Successfully!')
                return redirect('dashboard-homepage')
            else:
                slider_form = SliderForm()

        if 'whatwedo_form' in request.POST:
            whatwedo_form = WhatWeDoForm(request.POST)
            if whatwedo_form.is_valid():
                whatwedo_form.save()
                messages.success(request, 'What We Do Added Successfully!')
                return redirect('dashboard-homepage')
            else:
                whatwedo_form = WhatWeDoForm()

        if 'aboutus_form' in request.POST:
            aboutus_form = AboutUsForm(request.POST)
            if aboutus_form.is_valid():
                aboutus_form.save()
                messages.success(request, 'About Us Added Successfully!')
                return redirect('dashboard-homepage')
            else:
                aboutus_form = AboutUsForm()

    context = {
        'slider_form':slider_form,
        'whatwedo_form':whatwedo_form,
        'aboutus_form':aboutus_form,
    }

    return render(request,'dashboard/pages/dashboard_home.html',context)


@login_required(login_url='login')
def dashboard_blog(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Blog Post was successfully added')
            return redirect('dashboard-blog')
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request,'dashboard/pages/dashboard_blog.html',context)


@login_required(login_url='login')
def dashboard_gallery(request):
    return render(request,'dashboard/pages/dashboard_gallery.html')


@login_required(login_url='login')
def dashboard_mailing_list(request):
    return render(request,'dashboard/pages/dashboard_mailing_list.html')


@login_required(login_url='login')
def dashboard_procurement(request):
    return render(request,'dashboard/pages/dashboard_procurement.html')


@login_required(login_url='login')
def dashboard_inventory(request):
    inventories = Inventory.objects.all()

    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'New inventory was successfully added')
            return redirect('dashboard-inventory')

    else:
        form = InventoryForm()

    context = {
        'inventories': inventories,
        'form': form,
    }
    return render(request,'dashboard/pages/dashboard_inventory.html',context)

@login_required(login_url='login')
def dashboard_projects(request):
    projects = Footer.objects.all()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Project was successfully added')
            return redirect('dashboard-projects')
    else:
        form = ProjectForm()

    context = {
        'projects':projects,
        'form':form,
    }

    return render(request,'dashboard/pages/dashboard_projects.html',context)

@login_required(login_url='login')
def dashboard_register(request):
    return render(request,'dashboard/pages/dashboard_register.html')

@login_required(login_url='login')
def dashboard_stakeholders(request):
    return render(request,'dashboard/pages/dashboard_stakeholders.html')

@login_required(login_url='login')
def dashboard_website(request):
    return render(request,'dashboard/pages/dashboard_website.html')

@login_required(login_url='login')
def dashboard_homepage(request):
    return render(request,'dashboard/pages/dashboard_homepage.html')

@login_required(login_url='login')
def dashboard_contactus(request):
    # get the form populated with the last contact
    contact = Contact.objects.last()

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request,'Contact was successfully modified')
            return redirect('dashboard-contactus')
    else:
        form = ContactForm(instance=contact)

    context = {
        'form': form,
    }

    return render(request,'dashboard/pages/dashboard_contactus.html',context)

@login_required(login_url='login')
def dashboard_footer(request):
    footer = Footer.objects.last()

    if request.method == 'POST':
        form = FooterForm(request.POST, instance=footer)
        if form.is_valid():
            form.save()
            messages.success(request,'Footer was successfully modified')
            return redirect('dashboard-footer')
    else:
        form = FooterForm(instance=footer)

    context = {
        'form': form,
    }

    return render(request,'dashboard/pages/dashboard_footer.html',context)

@login_required(login_url='login')
def dashboard_faq(request):

    if request.method == 'POST':
        form = FaqsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'New faq was successfully added')
            return redirect('dashboard-faq')
    else:
        form = FaqsForm()

    context = {
        'form': form,
    }
    return render(request,'dashboard/pages/dashboard_faq.html',context)

@login_required(login_url='login')
def dashboard_career(request):
    if request.method == 'POST':
        form = CareerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'New job was successfully added')
            return redirect('dashboard-career')
    else:
        form = CareerForm()

    context = {
        'form': form,
    }
    return render(request,'dashboard/pages/dashboard_career.html',context)

@login_required(login_url='login')
def dashboard_testimonials(request):
    if request.method == 'POST':
        form = TestimonialsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'New testimonial was successfully added')
            return redirect('dashboard-testimonials')
    else:
        form = TestimonialsForm()

    context = {
        'form': form,
    }
    return render(request,'dashboard/pages/dashboard_testimonials.html',context)

@login_required(login_url='login')
def dashboard_aboutus(request):
    return render(request,'dashboard/pages/dashboard_aboutus.html')

@login_required(login_url='login')
def dashboard_team(request):
    if request.method == 'POST':
        form = TeamsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'New team member successfully added')
            return redirect('dashboard-team')
    else:
        form = TeamsForm()

    context = {
        'form': form,
    }

    return render(request,'dashboard/pages/dashboard_team.html',context)


@login_required(login_url='login')
def dashboard_staffs(request):
    staffs = Staff.objects.all()

    context = {
        'staffs':staffs,
    }

    return render(request,'dashboard/pages/dashboard_staffs.html',context)


# Login and Register
def registerPage(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CreateUserForm()

    return render(request,'account/register.html',{'form':form})


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('dashboard-home')

    else:
        if request.method == 'POST':

            uname = request.POST.get('username')
            passs = request.POST.get('password')

            user = authenticate(request,username=uname, password=passs)

            if user is not None:
                login(request,user)
                return redirect('dashboard-home')

        return render(request,'account/login.html')


def logoutUser(request):
    logout(request)
    return redirect ('login')
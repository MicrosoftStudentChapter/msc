from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .models import *
from .forms import *
from msc.settings import MEDIA_URL,MEDIA_ROOT
from django.contrib.auth import logout
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


User = get_user_model()
def home(request):
    team=Secretarie.objects.all()
    about=About_us.objects.all()
    events=Events.objects.all()
    post=Post.objects.all().order_by('-timestamp')
    Gallery_Img=index_gallery.objects.all()
    about_us_content=About_us_content.objects.all()
    heading_content=Heading_Content.objects.all()
    context={
    "core_team":team,
    "about_us_content":about_us_content,
    "abt":about,
    "evnt":events,
    "post" : post,
    "gall_img":Gallery_Img,
    "heading_content":heading_content,
    }
    return render(request, 'src/index.html',context)

def logout_view(request):
    logout(request)
    template = 'src/index.html'
    return render(request, template)

def team_page(request):
    technical=Team.objects.filter(department='1st')
    event_management=Team.objects.filter(department='2nd')
    creativity=Team.objects.filter(department='3rd')
    publicity=Team.objects.filter(department='4th')
    website=Team.objects.filter(department='5th')
    technical_head=Head_Team.objects.filter(department='1st')
    event_management_head=Head_Team.objects.filter(department='2nd')
    creativity_head=Head_Team.objects.filter(department='3rd')
    publicity_head=Head_Team.objects.filter(department='4th')
    social_head=Head_Team.objects.filter(department='5th')
    context = {
    "technical": technical,
    "event_management":event_management,
    "creativity":creativity,
    "publicity":publicity,
    "website":website,
    "technical_head": technical_head,
    "event_management_head":event_management_head,
    "creativity_head":creativity_head,
    "publicity_head":publicity_head,
    "social_head":social_head,
    }

    return render(request,'src/about_us.html',context)


def main_gallery(request):
    title= ": Gallery"
    msweek=MSWEEK_gallery.objects.all()
    inspirus=INSPIRUSUS_gallery.objects.all()
    rumble=RUMBLE_gallery.objects.all()
    context = {
    "title": title,
    "msweek":msweek,
    "inspirus":inspirus,
    "rumble":rumble,
    }

    return render(request, 'src/full_gallery.html',context)

def newsfeed(request):
    post=Post.objects.all()
    context= {
    "post":post,
    }

    return render(request,'src/newsfeed.html',context)


class DetailView(generic.DetailView):
    model=Post
    template_name = 'src/detail.html'

def msweek_event(request):
    title = "MS Week"
    events=MSWeek_Event.objects.all()
    context = {
    "title":title,
    "events":events
    }

    if(events):
        return render(request, 'src/events.html', context)
    else:
        return render(request, 'src/events_soon.html', context)

def inspirus_event(request):
    title = "INSPIRUS"
    events=Inspirus_Event.objects.all()
    context = {
    "title":title,
    "events":events
    }
    if(events):
        return render(request, 'src/events.html', context)
    else:
        return render(request, 'src/events_soon.html', context)

def rumble_event(request):
    title = "RUMBLE"
    events=Rumble_Event.objects.all()
    context = {
    "title":title,
    "events":events
    }

    if(events):
        return render(request, 'src/events.html', context)
    else:
        return render(request, 'src/events_soon.html', context)

def ContactView(request):
    title= ": Contact"
    context={
    "title":title,
    }

    return render(request,'src/contact3.html',context)

def secom(request):
    return render(request, 'src/secom.html')

def techmeet(request):
    return render(request, 'src/techmeet.html')




def event_registration(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'src/event_registration.html', {'form': form})
            # return redirect('post_detail', pk=post.pk)
    else:
        form = EventForm()
    return render(request, 'src/event_registration.html', {'form': form})

def registration(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'src/register.html', {'form': form})
            # return redirect('post_detail', pk=post.pk)
    else:
        form = registerForm()
    return render(request, 'src/register.html', {'form': form})


def ContactView(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'src/contact3.html', {'form': form})
            # return redirect('post_detail', pk=post.pk)
    else:
        form = ContactForm()
    return render(request, 'src/contact3.html', {'form': form})



def privacy(request):
    return render(request, 'src/privacy-policy.html')


def hacktoberfest(request):
    return render(request, 'src/hacktoberfest.html')

def hacktober_form(request):
    if request.method == "POST":
        form = hkctForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # messages.success(request, 'Form submission successful')
            # return redirect('post_detail', pk=post.pk)
    else:
        form = EventForm()
    return render(request, 'src/event_registration.html', {'form': form})

def hacktober_form2(request):
    if request.method == "POST":
        form = hkctForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # messages.success(request, 'Form submission successful')
            # return redirect('post_detail', pk=post.pk)
    else:
        form = EventForm()
    return render(request, 'src/event_registration2.html', {'form': form})

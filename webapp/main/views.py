# Plik do definiowania widoków, które są renderowane za pomocą szablonizatora Jinja oraz wyświetlane w przeglądarce

from django.shortcuts import render, redirect
from .forms import RegisterForm, AvatarForm
from django.contrib.auth import login, logout, authenticate
from news.models import Articles
from django.urls import reverse_lazy
from .models import Avatar, Event, Round
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View

# Create your views here.
def index(request):
    recent_articles = Articles.objects.all().order_by('-published_at')[:3]
    return render(request, 'main/index.html', {'recent_articles': recent_articles})


def events(request):
    events = Event.objects.prefetch_related('rounds').all()
    return render(request, 'main/events.html', {'events': events})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def sign_up (request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("/home")
    else:
        form = RegisterForm()

    return render(request, "registration/sign_up.html", {"form":form})

@method_decorator(login_required, name='dispatch')
class UploadOrUpdateAvatar(View):
    def get(self, request):
        avatar_instance = Avatar.objects.filter(user=request.user).first()
        form = AvatarForm(instance=avatar_instance)
        return render(request, 'main/upload_avatar.html', {'form': form})

    def post(self, request):
        avatar_instance, created = Avatar.objects.get_or_create(user=request.user)
        form = AvatarForm(request.POST, request.FILES, instance=avatar_instance)

        if form.is_valid():
            form.save()
            return redirect('/home')

        return render(request, 'main/upload_avatar.html', {'form': form})
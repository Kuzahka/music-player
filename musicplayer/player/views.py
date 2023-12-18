from django.shortcuts import render, redirect
from .forms import SongForm
from .models import Song
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm
from rest_framework import generics

from .models import Song
from .serializers import SongSerializer

def upload(request):
    if request.method == "POST":
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.DJ = request.user
            post.save()
            return redirect("player:index")
    else:
        form = SongForm()
    return render(request, "player/upload.html", {"form": form})


# this is for showing all songs on the home page
def index(request):
    if request.user.is_authenticated:
        songs = Song.objects.filter(DJ=request.user)
        return render(request, "player/index.html", {"songs": songs})
    else:
        return redirect('player:login')



class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('player:index')
    template_name = 'player/signup.html'


class SongList(generics.ListCreateAPIView):
    queryset =Song.objects.all()
    serializer_class = SongSerializer


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
# Create your views here.

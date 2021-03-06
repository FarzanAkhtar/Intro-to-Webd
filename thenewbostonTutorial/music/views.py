'''from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', { 'all_albums' : all_albums })

def detail(request, album_id):
    # Instead of this:
    # try  :
        # album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
        # raise Http404("Album does not exist")
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', { 'album' : album })

def favourite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
        'album' : album,
        'error_message' : "Select a valid song!!",
         })
    else:
        if selected_song.is_favourite:
            selected_song.is_favourite = False
        else:
            selected_song.is_favourite = True
        selected_song.save()
        return render(request, 'music/detail.html', { 'album' : album })
'''
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

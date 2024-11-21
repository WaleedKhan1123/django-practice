from django.shortcuts import render

from django.http import Http404
from .models import Note

databaseData = Note.objects.all()
def note(request):
    return render(request,'notes/Data.html',{'NotesData':databaseData})


def detail(request,pk):
    try:
      note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        raise Http404("Note does not exist")
    return render(request,'notes/details.html',{'note':note})
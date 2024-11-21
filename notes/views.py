from django.shortcuts import render

# Create your views here.
from .models import Note

databaseData = Note.objects.all()
def note(request):
    return render(request,'notes/Data.html',{'NotesData':databaseData})
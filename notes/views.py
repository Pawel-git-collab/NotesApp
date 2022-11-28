from django.shortcuts import render
from .models import Note
from .forms import NoteForm


def home(request):
    notes = Note.objects
    form = NoteForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    context = {'notes': notes, 'form': form}
    return render(request, 'home.html', context=context)



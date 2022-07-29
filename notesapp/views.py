from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.utils import timezone
import datetime as dt

from . import forms as note_forms
from .models import Note

# Create your views here.
def index(request):
    context = {}
    return render(request, "notesapp/index.html", context)

@require_http_methods(["GET", "POST"])
@login_required(login_url="accounts:login")
def add_note(request):
    if request.method == "POST":
        note_form = note_forms.NoteForm(request.POST)

        if note_form.is_valid():
            note_name = note_form.cleaned_data["name"]
            note_content = note_form.cleaned_data["name"]
            slug_title = note_form.cleaned_data["slug_title"]
            date_created = timezone.now()
            last_modified = timezone.now()

            new_note = Note(
                owner=request.user,
                name=note_name,
                content=note_content,
                slug_title=slug_title,
                date_created=timezone.now(),
                last_modified=timezone.now()
            )
            new_note.save()
            print("New note created!")
            return redirect("notesapp:view_notes")

        else:
            print("Invalid form")
            return redirect("notesapp:add_note")

    else:
        note_form = note_forms.NoteForm()
        context = {
            'note_form': note_form
        }
        return render(request, "notesapp/add_note.html", context)

@require_http_methods(["GET"])
@login_required(login_url="accounts:login")
def view_notes(request):
    notes_list = Note.objects.filter(owner=request.user)
    notes = notes_list.order_by('date_created').reverse()
    context = {
        'notes': notes,
        'note_count': len(notes)
    }
    return render(request, "notesapp/view_notes.html", context)

@require_http_methods(["GET"])
@login_required(login_url="accounts:login")
def view_note(request, slug_title):
    note = Note.objects.get(owner=request.user, slug_title=slug_title)
    context = {
        'note': note
    }
    return render(request, "notesapp/view_note.html", context)

@require_http_methods(["GET"])
@login_required
def delete_note(request, slug_title):
    note = Note.objects.get(owner=request.user, slug_title=slug_title)
    note.delete()
    print("Note deleted!")
    return redirect("notesapp:view_notes")
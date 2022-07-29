from django.urls import path
from . import views

app_name = "notesapp"
urlpatterns = [
    path('', views.index, name='index'),
    path('add-note', views.add_note, name="add_note"),
    path('view-notes', views.view_notes, name="view_notes"),
    path('view-note/<slug:slug_title>', views.view_note, name="view_note"),
    path('delete-note/<slug:slug_title>', views.delete_note, name="delete_note"),
]
from django import forms

class NoteForm(forms.Form):
    name = forms.CharField(label='Note title')
    content = forms.CharField(label='Note content', widget=forms.Textarea(attrs={'cols': '70', 'rows': '40'}))
    slug_title = forms.CharField(label='Slug title')
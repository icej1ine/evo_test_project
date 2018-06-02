import re

from django.shortcuts import render, redirect

from notes.models import Notes


def index(request):
    return render(
        request=request,
        template_name='index.html'
    )


def notes(request):

    return render(
        request=request,
        template_name='notes.html',
        context={'notes': Notes.objects.all()}
    )


def new_note(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        unique_text = set(re.findall(r"[\w']+", text.lower()))
        unique_count = len(unique_text)
        Notes.objects.create(text=text, unique_count=unique_count)
        # TODO remove hardcoded link
        return redirect('/notes')

    return render(
        request=request,
        template_name='new_note.html'
    )

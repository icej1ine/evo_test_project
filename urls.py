
from django.urls import path

from notes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes', views.notes, name='notes'),
    path('new_note', views.new_note, name='new_note'),
]

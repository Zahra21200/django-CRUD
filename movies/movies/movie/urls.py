from django.urls import path
from .views import *
urlpatterns = [
    path('List', movie_list,name='movie_list'),
    path('Add', add_movie, name='add_movie'),
    path('Update/<int:id>', update_movie, name='update_movie'),
    path('Delete/<int:id>', delete_movie, name='delete_movie'),
    path('Movie/<int:id>', display_movie, name='display_movie'),

]

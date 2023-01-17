from django.urls import path

from player.views.create_player_view import CreatePlayerView


urlpatterns = [
    path('create', CreatePlayerView.as_view()),
]
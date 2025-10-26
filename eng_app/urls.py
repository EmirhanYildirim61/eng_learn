from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('add-word/', views.add_word, name='add-word'),
    path('delete-word/', views.delete_word, name='delete-word'),
    path('learn-word/', views.learn_word, name='learn-word'),

    path('delete-word-action/<int:word_id>/', views.delete_word_action, name='delete-word-action'),
]

from django.urls import path

from sync import views

app_name = 'sync'
urlpatterns = [
    path('', views.index, name='index'),
    path('init', views.initialise, name='init'),
    path('update', views.update, name='update'),
]
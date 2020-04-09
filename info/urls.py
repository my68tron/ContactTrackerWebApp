from django.urls import path

from info import views

app_name = 'info'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('track/', views.track_user, name="track"),
]
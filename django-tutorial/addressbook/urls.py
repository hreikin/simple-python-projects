from django.urls import path

from . import views

app_name = 'addressbook'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
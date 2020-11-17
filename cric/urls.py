from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('match', views.match, name='match'),
    path('manage', views.manage, name='manage')


]

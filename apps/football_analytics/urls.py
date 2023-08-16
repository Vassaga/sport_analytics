

""" FOOTBALL URLS """


from django.urls import path

from . import views

urlpatterns = [
    path('football/', views.matches_list, name='matches_list')
]

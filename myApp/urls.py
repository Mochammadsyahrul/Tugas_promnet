from django.urls import path
from . import views
urlpatterns =[
    path('', views.index, name='index'),
    path('profil_saya', views.profil_saya, name='profil_saya'),
    path('sosmed', views.sosmed, name='sosmed'),
    path('pendidikan', views.pendidikan, name='pendidikan'),
    path('pengalaman', views.pengalaman, name='pengalaman'),
]
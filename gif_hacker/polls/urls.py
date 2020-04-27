from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_gif>/', views.detail, name='detail'),
    path('<int:id_gif>/results/', views.results, name='results'),
    path('<int:id_gif>/vote/', views.vote, name='vote')
]
from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_gif>/like/', views.like, name='like'),
    path('<int:id_gif>/deslike/', views.deslike, name='deslike')
]
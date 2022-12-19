from django.urls import path
from movieapp import views
from movieapp.views import update
app_name='movieapp'
urlpatterns = [

    path('', views.demo, name='demo'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]

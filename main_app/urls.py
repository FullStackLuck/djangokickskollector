from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name= 'about'),
    path('kicks/', views.kicks_index, name= 'index'),
    path('kicks/<int:kick_id>/', views.kicks_detail, name='detail'),
    path('kicks/create/', views.KickCreate.as_view(), name='kick_create'),
    path('kicks/<int:pk>/update/', views.KickUpdate.as_view(), name='kick_update'),
    path('kicks/<int:pk>/delete/', views.KickDelete.as_view(), name='kick_delete'),
]
from django.urls import path
from .import views

urlpatterns =[
    path('media/',views.MediaSourceList.as_view(),name='media'),
    path('media/<int:pk>/',views.MediaSourceDetailView.as_view(),name='media-detail'),

]
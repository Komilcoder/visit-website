from django.urls import path
from .import views 


urlpatterns = [
    path('profile/',views.ProfileList.as_view(),name='profile'),
    path('profile/<int:pk>/',views.ProfileDetailView.as_view(),name='profile-detail'),
    path('image/',views.ProfileListImageView.as_view(),name='profile-image'),
    path('image/<int:pk>/',views.ProfileImageView.as_view(),name='profile-detail'),
    
    
]
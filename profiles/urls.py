from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.UserProfileListCreate.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', views.UserProfileRetrieveUpdateDestroy.as_view(), name='profile-detail'),
]

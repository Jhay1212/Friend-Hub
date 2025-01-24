from django.urls import path
from . import views

urlpatterns =[
    path('<slug:slug>', views.ProfileView.as_view(), name='profile'),
]
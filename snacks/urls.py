from django.urls import path
from .views import SnackListView,SnackDetailsView,HomeView

urlpatterns = [
path('',HomeView.as_view(), name='Home'),
path('snacks/',SnackListView.as_view(), name='snacks'),
path('snacksdetails/',SnackDetailsView.as_view(), name='snack_details'),



]

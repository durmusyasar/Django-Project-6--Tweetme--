from django.urls import path
from django.views.generic.base import RedirectView

from .views import (
    UserDetailView,
    UserFollowView
)

app_name = 'profiles'

urlpatterns = [
    path('<username>/', UserDetailView.as_view(), name='detail'),
    path('<username>/follow/', UserFollowView.as_view(), name='follow'),
] 

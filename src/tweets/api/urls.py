from django.urls import path
from django.views.generic.base import RedirectView

from .views import (
    TweetListAPIView,
    RetweetAPIView,
    TweetCreateAPIView,
    LikeToggleAPIView,
    TweetDetailAPIView,
)

app_name = 'api-tweet'

urlpatterns = [
    path('<pk>/', TweetDetailAPIView.as_view(), name='detail'),
    path('', TweetListAPIView.as_view(), name='list'),
    path('create/', TweetCreateAPIView.as_view(), name='create'),
    path('<pk>/retweet/', RetweetAPIView.as_view(), name='retweet'),
    path('<pk>/like/', LikeToggleAPIView.as_view(), name='like-toggle'),
] 

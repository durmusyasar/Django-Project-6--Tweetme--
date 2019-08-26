from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import UserRegisterView
from hashtags.views import HashTagView
from hashtags.api.views import TagTweetAPIView
from tweets.api.views import SearchTweetAPIView
from .views import home, SearchView
from tweets.views import TweetListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TweetListView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search'),
    path('tags/<hashtag>/', HashTagView.as_view(), name='hashtag'),
    path('tweet/', include('tweets.urls')),
    path('api/tags/<hashtag>/', TagTweetAPIView.as_view(), name='tag-tweet-api'),
    path('api/search/', SearchTweetAPIView.as_view(), name='search-api'), 
    path('api/tweet/', include('tweets.api.urls')),
    path('api/', include('accounts.api.urls')),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
    path('', include('accounts.urls')),
] 
if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('programs', views.programs, name='programs'),
    path('enter-coaching', views.enter_coaching, name='enter-coaching'),
    path('science-and-art', views.science_and_art, name='science-and-art'),
    path('team-coaching', views.team_coaching, name='team-coaching'),
    path('upraclencheskiy', views.upraclencheskiy, name='upraclencheskiy'),
    path('feed-list', views.feed_list, name='feed_list'),
    path('review/<int:id>', views.feed_detail, name='feed_detail'),
    path('coaches', views.coaches, name='coaches'),
    path('coaches/<int:id>', views.coaches_detail, name='coaches_detail'),
    path('games', views.games, name='games'),
    path('games/<int:id>', views.games_detail, name='games_detail'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('timetable', views.timetable, name='timetable'),
    path('timetable-filter', views.timetable_filter, name='timetable_filter'),
    path('coaching', views.coaching, name='coaching'),
    path('article', views.news, name='article'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

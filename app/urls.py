from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('feed-list', views.feed_list, name='feed_list'),
    path('review/<int:id>', views.feed_detail, name='feed_detail'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
